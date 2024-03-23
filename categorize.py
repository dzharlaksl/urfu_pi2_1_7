# Функция для категоризации и приоритизации запросов в техподдержку
def categorize_ticket(ticket):
    # Определение категорий и приоритетов с ассоциированными ключевыми словами
    categories = {        
        1: ['банк', 'платеж', 'транзакц', 'финанс', 'деньг'], # 'Финансовая система'
        2: ['интернет', 'сеть', 'соединение', 'доступ', 'сервер'], # 'Сетевая проблема'
        3: ['email', 'имейл', 'почт', 'письмо', 'spam', 'сообщение'], # 'Почта'
        4: ['звонок', 'телефон', 'связь', 'оператор', 'сигнал'], # 'Связь'
        5: ['принтер', 'клавиатур', 'мыш', 'клавиш', 'монитор', 'диспле', 'печат', 'бумаг', 'картридж', 'замятие'], # 'Техника'
        6: ['вирус', 'защитник', 'касперск', 'троян'], #'Безопасность'
        7: ['windows', 'виндус', 'винда', 'виндоус', 'linux', 'линукс', 'обновлен','грузит'], # 'Операционная система'
        8: ['Word', 'ворд', 'Excel', 'эксель', 'Point', 'Power', 'пауэр', 'поинт'] #'Office'
    }
    
    # Определение приоритетов с ассоциированными ключевыми словами
    priorities = {
        1: ['срочно', 'немедленно', 'важно', 'критический', 'падение'],
        2: ['задержка', 'проблема', 'ошибка', 'неудобство', 'ожидание'],
        3: ['запрос', 'вопрос', 'предложение', 'информация', 'уточнение']
    }
    
    # Инициализация категории и приоритета
    ticket_category = 0
    ticket_priority = 3

    # Проверка ключевых слов категории
    for category, keywords in categories.items():
        if any(keyword in ticket.lower() for keyword in keywords):
            ticket_category = category
            break
        
    # Проверка ключевых слов приоритета
    for priority, keywords in priorities.items():
        if any(keyword in ticket.lower() for keyword in keywords):
            ticket_priority = priority
            break
    
    print("-"*100)
    print("ТЕКСТ ТИКЕТА = "+str(ticket))
    print("КАТЕГОРИЯ = "+str(ticket_category))
    print("ПРИОРИТЕТ = "+str(priority))    
    # Создание краткого названия исходного запроса
    #ticket_summary = ' '.join(ticket.split()[:5]) + '...' if len(ticket.split()) > 5 else ticket
    return {"ticket_text":ticket, "category":ticket_category, "priority": ticket_priority}
        


# Функция теста работопособности
if __name__ == '__main__':
    # Пример входных данных
    tickets = [
        "Не могу отправить email, возможно проблемы с сервером",
        "Принтер показывает ошибку и не печатает",
        "Система платежей выдает сбой при попытке транзакции",
        "Телефон не ловит сигнал, возможно проблемы со связью"
    ]

    # Вызов функции и вывод результатов
    for ticket in tickets:
        print(categorize_ticket(ticket))