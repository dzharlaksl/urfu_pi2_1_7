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


@st.cache_resource
def load_modeltr():
    """
    Вызываем функцию загрузки модели
    Кешируем загрузку модели (экономия ресурсов) через @st.cache_resource
    """
    return load_model()

# функция вывода полученых данных
# это временная функция. Будет разработан отдельный интерфейс отображения задачи, приоритета, категории
def output_data(ticket_data):
    st.write("Текст тикета:      "+ticket_data["ticket_text"])
    st.write("Категория задачи:  "+ticket_data["category"])
    st.write("Категория задачи:  "+ticket_data["priority"])


if __name__ == '__main__':
    # выводим приверственный тайтл и кратко обозначаем функционал приложения
    st.title('AI генератор задач для техподдержки')
    st.write("""На основании аудиозаписи автоответчика службы поддержки
             производится перевод аудио в текст, а также определение
             категории задачи и ее приоритета""")

    audio_file = st.file_uploader('Загрузите аудиофайл',
                                  #type=['mp3', 'm4a', 'flac'],
                                  type=['flac'],
                                  accept_multiple_files=False, key=None,
                                  on_change=None)

    # предлагаем пользователю выбрать, локально запускаем модель или по API
    option = st.selectbox(
        'Локальный запуск распознавания или используем API?',
        ('Локально', 'API'), key='option')

    btn1 = st.button("Поехали!", key="summ", type="primary")    

    if btn1:
        if audio_file:
            if option == 'Локально':
                st.write('Локальный запуск')
                # загружаем модель
                model = load_modeltr()
                # вызываем функцию транскрибации текста
                ticket_text = transcribe(model, audio_file)
                ticket_data = categorize_ticket(ticket_text)
                #ticket_data = {"ticket_text":ticket_text, "category":"категория", "priority": "приоритет 1"}

            else:
                st.write('Используем API')
                # вызываем API метод, в который передаем аудио запись            
                # ticket_data = get_ticket_api(audio_file)
                ticket_text = "Здесь будет текст, который вернет API"
                #ticket_data = categorize_tickets(ticket_text)
                ticket_data = {"ticket_text":ticket_text, "category":"категория", "priority": "приоритет 1"}
            # функция вывода тикета на фронт
            output_data(ticket_data)

        else:
            st.write('Пожалуйста, загрузите аудиофайл')

        
