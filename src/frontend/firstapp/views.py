from django.shortcuts import render
from .forms import NewEmployeeForm, NewClientForm, CreateTicketForm
from .demo import create_demo_category, create_demo_clients
from .demo import create_demo_employee, create_demo_ticket
from .models import Client, Employee, Category, Ticket
from random import randint
from datetime import datetime
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from transcribe import transcribe, load_model  # noqa: E402
from categorizer import categorize_ticket  # noqa: E402


# стартовая страница с информацией о проекте и ссылками на основные функции
def index(request):
    """
    Вызывается при запросе пользователем в браузере стартовой страницы веб-интерфейса (URL / )

    Args:
        request (obj): POST либо GET запрос, переданный браузером

    Returns:
        вызывается функция отрисовки темплейта index.html
    """
    return render(request, "index.html")


# функция создания нового клиента в БД
def create_client(request):
    """
     Вызывается при запросе пользователем в браузере страницы
     создания клиента URL /create_clients

    Args:
        request (obj): POST либо GET запрос, переданный браузером

    Returns:
        вызывается функция отрисовки темплейта newuser.html
    """

    if request.method == "POST":
        newclient = Client()
        newclient.phone = request.POST.get("phone")
        newclient.email = request.POST.get("email")
        newclient.fname = request.POST.get("fname")
        newclient.lname = request.POST.get("lname")
        newclient.save()

        return render(request, "success.html", {"item": "клиент"})
    else:
        newclientform = NewClientForm()
        return render(request, "newuser.html",
                      {"item": "клиент", "form": newclientform})


# внесение информации о новом сотруднике в базу данных
def create_employee(request):
    """
     Вызывается при запросе пользователем в браузере страницы
     создания сотрудника URL /create_employee

    Args:
        request (obj): POST либо GET запрос, переданный браузером

    Returns:
        вызывается функция отрисовки темплейта newuser.html
        либо success.html - когда данные валидные и сотрудник создан в БД
    """

    newempform = NewEmployeeForm(request.POST or None)

    # проверяем валидность введенных пользователем данных в форму
    if newempform.is_valid():
        # пользователь ввел корректные данные, значит создаем объект класса Employee
        newemployee = Employee()

        # вносим данные из форм заполненных пользователем в поля объекта класса, для последующей записи в БД
        newemployee.fname = request.POST.get("fname")
        newemployee.lname = request.POST.get("lname")
        newemployee.phone = request.POST.get("phone")
        newemployee.email = request.POST.get("email")

        try:
            # пытаемся найти категорию в БД
            newemployee.category = Category.objects.get(id=request.POST.get("category"))
        except Category.DoesNotExist:
            # если категорию в БД не находим, то записываем категорию по-умолчанию
            newemployee.category = Category.objects.get(id=0)
            # и выводим сообщение об ошибке в веб-форму
            data = {"form": newempform,
                    "errormes": "Категория " + request.POST.get("category") + " не найдена в базе данных!"}
            return render(request, "create_ticket.html", context=data)

        # если дошли до этого момента, значит с данными все впорядке, поля заполненны, сохраняем запись в БД
        newemployee.save()

        # перекидываем пользователя на страничку "успеха"
        return render(request, "success.html", {"item": "сотрудник"})
    else:
        # пользователь ввел невалидные данные, либо получен запрос GET
        # т.е. пользователь зашел первый раз на страницу и никакие данные еще не отправлял,
        # иначе сработал бы метод POST
        return render(request, "newuser.html",
                      {"item": "сотрудник", "form": newempform})


# создание новой задачи (тикета)
def create_ticket(request):
    """
     Вызывается при запросе пользователем в браузере страницы
     создания нового тикета URL /create_ticket. Выводит пользователю
     форму ввода данных по заявке.
     Заявку можно внести вручную, заполнив все поля, а можно
     указать только телефон клиента (имеющийся в базе) и
     загрузить аудиофайл в формате flac.
     Во втором случае аудиозапись будет переведена в текст,
     определена категория задачи и приоритет. На основании категории
     будет подобран сотрудник поддержки (рандомом из выборки по БД),
     который спецализируется на данной категории задач

    Args:
        request (obj): POST либо GET запрос, переданный браузером

    Returns:
        вызывается функция отрисовки темплейта create_ticket.html
    """

    # передаем в форму данные полученные из метода POST и файлы.
    # это на тот случай, если пользовтаель уже ввел какие-то данные, но они оказались невалидными
    # и чтобы заново все не вносить, мы возвращаем в форму ранее заполненные пользователем данные
    form = CreateTicketForm(request.POST or None, request.FILES or None)

    # проверяем валидность введенных в форму данных
    # (при первом запуске функции данные не валидны, поскольку их еще нет)
    if form.is_valid():

        # пользователь ввел валидные данные в поля формы - создаем экземпляр класса Ticket и записываем его в БД
        newticket = Ticket()
        newticket.tdate = datetime.now()

        if form.cleaned_data['audio_ticket']:
            newticket.audio_ticket = form.cleaned_data['audio_ticket']
            ticket_data = categorize_ticket(transcribe(MODEL, newticket.audio_ticket))
            newticket.text_ticket = ticket_data["ticket_text"]
            category = ticket_data["category"]
            priority = ticket_data["priority"]
        else:
            newticket.text_ticket = request.POST.get("text_ticket")
            category = int(request.POST.get("category"))
            priority = int(request.POST.get("priority"))

        newticket.priority = priority

        # по email клиента пытаемся найти его в БД и в заявке указываем объект Клиент
        try:
            cl = Client.objects.get(phone=request.POST.get("phone"))
            newticket.client = cl
        except Client.DoesNotExist:
            # если клиент по номеру телефона не нашелся, выводим сообщение об ошибке в консоль и на веб-форму
            print("Клиент в базе не найден. Проверьте корректность введенного номера телефона")
            data = {"form": form,
                    "errormes": "Клиент в базе не найден. Проверьте корректность введенного номера телефона!"}
            return render(request, "create_ticket.html", context=data)

        # пытаемся найти категорию в смежной таблице БД
        try:
            newticket.category = Category.objects.get(id=category)
        except Category.DoesNotExist:
            # если категорию не находим, то указываем категорию по-умолчанию
            newticket.category = Category.objects.get(id=0)
            data = {"form": form,
                    "errormes": "Категория " + request.POST.get("category") + " не найдена в базе данных!"}
            return render(request, "create_ticket.html", context=data)

        # подбираем сотрудника под задачу. Выгружаем всех сотрудников с требуемым типом задачи
        emp = Employee.objects.filter(category_id=category)
        if emp.count() > 0:
            # рандомно выбираем сотрудника из выборки подходящих
            newticket.employee = emp[randint(0, emp.count()-1)]
        else:
            # если сотрудника не находим, то указываем неопределенного сотрудника (специально создан для этого в БД)
            newticket.employee = Employee.objects.get(id=0)

        # сохраняем объект (новую заявку) в базе данных
        newticket.save()
        return render(request, "success.html", {"item": "тикет"})

    else:
        # пользователь ввел невалидные данные в форму, либо произошел первый запуск формы
        print(form.errors)
        return render(request, "create_ticket.html", context={"form": form})


# отображение списка всех тикетов (заданий)
def tickets(request):
    """
     Вызывается при запросе пользователем в браузере страницы
     вывода всех заявок в поддержку URL /tickets.
     Заявки "вынимаются" из БД и отображаются в виде таблицы

    Args:
        request (obj): POST либо GET запрос, переданный браузером

    Returns:
        вызывается функция отрисовки темплейта tickets.html
    """
    return render(request, "tickets.html", context={"tikets": Ticket.objects.all()})


MODEL = load_model()
print("Модель загружена: ", MODEL)
print("+"*100)
print("Добавлен системный путь: ", Path(__file__).resolve().parent.parent.parent)
print("+"*100)
create_demo_category()
create_demo_clients()
create_demo_employee()
create_demo_ticket()
