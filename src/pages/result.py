import streamlit as st
from set import categories, priorities

# Если нет данных, переключаемся на главную страницу
if "ticket_data" not in st.session_state or "audio_file" not in st.session_state:
    st.switch_page("frontend.py")

# Получаем данные
ticket_data = st.session_state["ticket_data"]
audio_file = st.session_state["audio_file"]

st.title(f'Результат обработки файла {audio_file.name}')

# выводим данные
st.write(f"Категория задачи: **{categories[ticket_data['category']]}**")
st.write(f"Приоритет задачи: **{priorities[ticket_data['priority']]}**")
st.write(f"Текст тикета: **{ticket_data['ticket_text']}**")

# При необходимости можно послушать аудио
st.audio(audio_file, format='audio/ogg')

# возврат на главную страницу
if st.button("Загрузить другой файл"):
    st.switch_page("frontend.py")
