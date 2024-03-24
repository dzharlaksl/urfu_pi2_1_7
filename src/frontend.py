"""
Проект: расшифровка сообщений с автоответчика (из аудио файла в текст)
и создание заявок на основе сообщения.
Веб-интерфейс
Программная инженерия, группа 1.7
"""

# импортируем необходимые бибилиотеки
import streamlit as st
from transcribe import transcribe, load_model
from categorizer import categorize_ticket
from set import categories, priorities


@st.cache_resource
def load_modeltr():
    """
    Вызываем функцию загрузки модели
    Кешируем загрузку модели (экономия ресурсов) через @st.cache_resource
    """
    return load_model()


# функция вывода полученых данных - временный интерфейс
def output_data(ticket_data):
    st.write("Текст тикета:      "+ticket_data["ticket_text"])
    st.write("Категория задачи:  "+categories[ticket_data["category"]])
    st.write("Приоритет задачи:  "+priorities[ticket_data["priority"]])


if __name__ == '__main__':
    # выводим приверственный тайтл и кратко обозначаем функционал приложения
    st.title('AI генератор задач для техподдержки')
    st.write("""На основании аудиозаписи автоответчика службы поддержки
             производится перевод аудио в текст, а также определение
             категории задачи и ее приоритета""")

    audio_file = st.file_uploader('Загрузите аудиофайл',
                                  type=['flac'],
                                  accept_multiple_files=False, key=None,
                                  on_change=None)

    # предлагаем пользователю выбрать, локально запускаем модель или по API
    option = st.selectbox(
        'Локальный запуск распознавания или используем API?',
        ('Локально', 'API'), key='option')

    # добавляем кнопку в интерфейс
    btn1 = st.button("Поехали!", key="summ", type="primary")

    # проверям факт нажатия кнопки пользоваталем
    if btn1:
        # кнопка нажата, аудиофайл загружен
        if audio_file:
            # проверям выбор пользоваталем чекбокса (локально, или по API?)
            if option == 'Локально':
                # пользователь выбрал Локально
                st.write('Локальный запуск')
                # загружаем модель
                model = load_modeltr()
                # вызываем функцию транскрибации текста
                ticket_text = transcribe(model, audio_file)
                # вызываем функцию категоризации и приоритезации задачи
                ticket_data = categorize_ticket(ticket_text)
            else:
                # пользователь выбрал "API"
                st.write('Используем API')
                # вызываем API метод, в который передаем аудио запись
                # и получаем обратно текст, категорию и приритет
                # !!!!!!!!!!!!!!!!!!! ЗАГЛУШКА НАЧАЛО !!!!!!!!!!!!!!!!!!!!!!!!!!!
                # ticket_data = get_ticket_api(audio_file)                
                ticket_data = {"ticket_text": "Здесь будет какой текст, который вернет API",
                               "category": 0, "priority": 0}
                # !!!!!!!!!!!!!!!!!!! ЗАГЛУШКА КОНЕЦ !!!!!!!!!!!!!!!!!!!!!!!!!!!

            # ЗДЕСЬ ВЫЗЫВАЕТСЯ ФУНКЦИЯ ВЫВОДА ТИКЕТА НА ФРОНТ!!!
            output_data(ticket_data)

        else:
            # указываем пользователю на то, что он не загрузил файл!
            st.write('Пожалуйста, загрузите аудиофайл')
