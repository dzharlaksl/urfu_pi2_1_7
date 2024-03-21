# Функция для категоризации и приоритизации запросов в техподдержку
def categorize_tickets(tickets):
    # Определение категорий и приоритетов с ассоциированными ключевыми словами
    categories = {
        'Финансовая система': ['банк', 'платеж', 'транзакция', 'финанс', 'деньги'],
        'Сетевая проблема': ['интернет', 'сеть', 'соединение', 'доступ', 'сервер'],
        'Почта': ['email', 'почта', 'письмо', 'spam', 'сообщение'],
        'Связь': ['звонок', 'телефон', 'связь', 'оператор', 'сигнал'],
        'Факс': ['факс', 'документ', 'отправка', 'получение', 'линия'],
        'Принтер': ['принтер', 'печать', 'бумага', 'картридж', 'замятие'],
        'Операционная система': ['windows', 'linux', 'macos', 'обновление', 'сбой']
    }
    
    # Определение приоритетов с ассоциированными ключевыми словами
    priorities = {
        'Высокий': ['срочно', 'немедленно', 'важно', 'критический', 'падение'],
        'Средний': ['задержка', 'проблема', 'ошибка', 'неудобство', 'ожидание'],
        'Низкий': ['запрос', 'вопрос', 'предложение', 'информация', 'уточнение']
    }
    
    # Инициализация списка результатов
    output = []
    
    # Обработка каждого запроса
    for ticket in tickets:
        # Инициализация категории и приоритета
        ticket_category = 'Неопределенная категория'
        ticket_priority = 'Неопределенный приоритет'
        
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
        
        # Создание краткого названия исходного запроса
        ticket_summary = ' '.join(ticket.split()[:5]) + '...' if len(ticket.split()) > 5 else ticket
        
        # Добавление результата в список вывода
        output.append(f"{ticket_summary} | {ticket_category} | {ticket_priority}")
    
    # Возврат списка результатов
    return output

# Пример входных данных
tickets = [
    "Не могу отправить email, возможно проблемы с сервером",
    "Принтер показывает ошибку и не печатает",
    "Система платежей выдает сбой при попытке транзакции",
    "Телефон не ловит сигнал, возможно проблемы со связью"
]

# Вызов функции и вывод результатов
categorized_tickets = categorize_tickets(tickets)
for result in categorized_tickets:
    print(result)
