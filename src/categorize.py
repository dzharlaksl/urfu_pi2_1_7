import re
from collections import namedtuple

import pymorphy2


def words_from_text(text):
    """
    Функция возвращает список слов, приведенных к нормальной форме.

    Args:
        text (str): текст, из которого извлекаются слова

    Returns:
        list: массив слов в нормальной форме
    """
    clean_text = text.lower()

    clean_text = re.sub(r'[^\w\s]', ' ', clean_text)  # Убираем пунктуацию
    clean_text = re.sub(r'\s{2,}', ' ', clean_text)  # Убираем лишние пробелы

    legal_word = []
    for category in categories.values():
        legal_word.extend(category.key_words)

    # Убираем короткие слова, в основном предлоги, но сохраняем исключения, например "IP"
    words = [word for word in clean_text.split() if len(word) > 2 or word in legal_word]

    normal_words = []
    morph = pymorphy2.MorphAnalyzer()
    for word in words:
        normal_words.append(morph.parse(word)[0].normal_form)

    return normal_words


# Функция для определения категории по ключевым словам
def categorize_text(text):
    """
    Функция определяет категорию к которой относится текст.
    Для определения наиболее подходящей категории используется
    подобие Жаккара.

    Args:
        text (str): текст, для которого определяем категорию

    Returns:
        int: id категории, к которой относится текст
    """

    normal_words = words_from_text(text)
    A = set(normal_words)
    best_cat = 0
    best_score = 0

    for id_cat, category in categories.items():
        B = set(category.key_words)
        if len(A.union(B)) > 0:
            score = len(A.intersection(B))/len(A.union(B))
        else:
            score = 0
        if score > best_score:
            best_score = score
            best_cat = id_cat

    return best_cat


def category_name(id):
    """
    Функция возвращает название по числовому id

    Args:
        id (int): id категории

    Returns:
        str: название категории
    """
    return categories[id].name


def determine_priority(text):
    """
    Функция для определения приоритета текста на основе его эмоциональной окраски

    Args:
        text (str): текст для анализа

    Returns:
        int: id приоритета
    """

    normal_words = words_from_text(text)
    A = set(normal_words)
    best_priority = 0
    best_score = 0

    for id_priority, priority in priorities.items():
        B = set(priority.key_words)

        if len(A.union(B)) > 0:
            score = len(A.intersection(B))/len(A.union(B))
        else:
            score = 0

        if score > best_score:
            best_score = score
            best_priority = id_priority

    return best_priority


def priority_name(id):
    """
    Функция возвращает название приоритета по числовому id

    Args:
        id (int): id приоритета

    Returns:
        str: название приоритета
    """
    return priorities[id].name


# Основная функция скрипта
def ticket_info(text):
    """
    Определяет категорию и приоритет заявки по тексту

    Args:
        text (str): текст заявки

    Returns:
        dict:
            category (int): id категории
            priority (int): id приоритета
    """

    category = categorize_text(text)
    priority = determine_priority(text)

    return {"category": category, "priority": priority}


# Категории и приоритеты
Category = namedtuple("Category", "name key_words")
Priority = namedtuple("Priority", "name key_words")

categories = {
    0: Category(
        "Не определено", [],
    ),
    1: Category(
        "Финансовая система",
        [
            "деньги",
            "бюджет",
            "финансы",
            "инвестиции",
            "акции",
            "банк",
            "экономика",
            "доход",
            "расход",
            "налоги",
            "кредит",
            "депозит",
            "валюта",
            "облигации",
            "страхование",
            "рентабельность",
            "ликвидность"
        ],
    ),
    2: Category(
        "Сетевая проблема",
        [
            "сеть",
            "интернет",
            "соединение",
            "маршрутизатор",
            "сервер",
            "ip",
            "vpn",
            "протокол",
            "шифрование",
            "порт",
            "wi-fi",
            "lan",
            "wan",
            "пинг",
            "трафик",
            "брандмауэр",
            "dns",
            "провайдер"
        ],
    ),
    3: Category(
        "Почта",
        [
            "почта",
            "письмо",
            "вложение",
            "спам",
            "рассылка",
            "smtp",
            "imap",
            "фильтрация",
            "адресат",
            "отправитель",
            "тема",
            "подпись",
            "автоответчик",
            "рассылка",
            "конфиденциальность",
            "уведомление"
        ],
    ),
    4: Category(
        "Связь",
        [
            "связь",
            "телефон",
            "мобильный",
            "оператор",
            "сигнал",
            "звонок",
            "sms",
            "роуминг",
            "sim-карта",
            "lte",
            "4g",
            "5g",
            "сотовый",
            "станция",
            "абонент",
            "тариф",
            "минуты",
            "сообщение",
            "передача"
        ],
    ),
    5: Category(
        "Техника",
        [
            "техника",
            "компьютер",
            "принтер",
            "сканер",
            "ноутбук",
            "монитор",
            "диск",
            "usb",
            "мышь",
            "клавиатура",
            "процессор",
            "видеокарта",
            "ram",
            "память",
            "ssd",
            "hdd",
            "плата",
            "питание",
            "устройство",
            "гаджет"
        ],
    ),
    6: Category(
        "Безопасность",
        [
            "безопасность",
            "вирус",
            "антивирус",
            "шпионское по",
            "фишинг",
            "хакер",
            "защита данных",
            "шифрование",
            "пароль",
            "доступ",
            "биометрия",
            "отпечаток",
            "лицензия",
            "бэкап",
            "восстановление",
            "доступ",
            "аудит",
            "угроза"
        ],
    ),
    7: Category(
        "Операционная система",
        [
            "операционный",
            "windows",
            "linux",
            "macos",
            "обновление",
            "установка",
            "драйвер",
            "системный",
            "файл",
            "реестр",
            "терминал",
            "интерфейс",
            "gui",
            "процесс",
            "задача",
            "память",
            "настройка",
            "журнал"
        ],
    ),
    8: Category(
        "Office",
        [
            "office",
            "word",
            "excel",
            "powerpoint",
            "outlook",
            "редактирование",
            "таблица",
            "презентация",
            "документ",
            "шаблон",
            "форматирование",
            "диаграмма",
            "график",
            "макрос",
            "функция",
            "формула",
            "сортировка",
            "фильтрация"
        ],
    ),
}

priorities = {
    0: Priority("Не определен", []),
    1: Priority(
        "Высокий",
        [
            "срочно",
            "немедленно",
            "важно",
            "критический",
            "неотложный",
        ],
    ),
    2: Priority(
        "Средний",
        [
            "проблема",
            "задержка",
            "необходимо",
            "требуется",
            "ожидается",
        ],
    ),
    3: Priority(
        "Низкий",
        [
            "информация",
            "запрос",
            "пожелание",
            "рекомендация",
            "уведомление",
        ],
    ),
}
