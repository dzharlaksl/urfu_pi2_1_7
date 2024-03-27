"""
Проект: расшифровка сообщений с автоответчика (из аудио файла в текст)
и создание заявок на основе сообщения.
Веб-интерфейс
Программная инженерия, группа 1.7
"""

# импортируем необходимые бибилиотеки
import streamlit as st
from transcribe import transcribe, load_model
from categorize import ticket_info
import requests

API_URL = 'http://127.0.0.1:8008/ticket-info/'


@st.cache_resource
def load_modeltr():
    """
    Вызываем функцию загрузки модели
    Кешируем загрузку модели (экономия ресурсов) через @st.cache_resource
    """
    return load_model()


# функция вывода полученых данных - переключает на страницу результата
def output_data(ticket_data):
    st.session_state["ticket_data"] = ticket_data
    st.switch_page("pages/result.py")


def api_ticket_info(audio_file):
    files = {'audio_file': audio_file}
    response = requests.post(API_URL, files=files)
    return response.json()


if __name__ == '__main__':
    # выводим приветственный тайтл и кратко обозначаем функционал приложения
    st.title('AI генератор задач для техподдержки')
    st.write("""На основании аудиозаписи автоответчика службы поддержки
             производится перевод аудио в текст, а также определение
             категории задачи и ее приоритета""")

    audio_file = st.file_uploader('Загрузите аудиофайл',
                                  type=['flac'],
                                  accept_multiple_files=False, key='audio_file',
                                  on_change=None)

    # предлагаем пользователю выбрать, локально запускаем модель или по API
    option = st.radio(
        'Локальный запуск распознавания или используем API?',
        ('Локально', 'API'))

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
                with st.status("Анализируем файл...", expanded=True) as status:
                    st.write("Загружаем модель...")
                    # загружаем модель
                    model = load_modeltr()
                    st.write("Распознаем речь...")
                    # вызываем функцию транскрибации текста
                    text = transcribe(model, audio_file)
                    st.write("Анализируем текст...")
                    # вызываем функцию категоризации и приоритезации задачи
                    ticket_data = ticket_info(text)
                    ticket_data['text'] = text
            else:
                # пользователь выбрал "API"
                st.write('Используем API')
                with st.status("Анализируем файл...", expanded=True) as status:
                    st.write("Отправляем API запрос...")
                    # вызываем API метод, в который передаем аудио запись
                    # и получаем обратно текст, категорию и приоритет
                    ticket_data = api_ticket_info(audio_file)

            # ЗДЕСЬ ВЫЗЫВАЕТСЯ ФУНКЦИЯ ВЫВОДА ТИКЕТА НА ФРОНТ!!!
            output_data(ticket_data)

        else:
            # указываем пользователю на то, что он не загрузил файл!
            st.write('Пожалуйста, загрузите аудиофайл')
