# Import библиотеки для создания API и загрузки файла
from fastapi import FastAPI, UploadFile
# Import функций с моделями
from transcribe import load_model, transcribe  # Функция перевода аудио в текст
# Функция определения категории и приоритетности запроса по тексту
from categorize import categorize_ticket

app = FastAPI()  # Создаем приложение в переменной app
model = load_model()  # Загружаем модель в переменную model


@app.post("/model/")
async def process(audio_file: UploadFile):
    """Функция обработки аудио-файла.
    Читает переданный файл, передает его сначала в функцию перевода аудио в текст,
    затем передает текст в функцию категоризации.

    Args:
        audio_file (UploadFile): Аудио-файл

    Returns:
        Текст в формате JSON, где:
        Transcription - текст из аудио,
        Category - категория тикета,
        Priority - приоритет тикета.
    """
    content = audio_file.file.read()
    transcription = transcribe(model, content)
    categorization = categorize_ticket(transcription)
    return {"Transcription": transcription,
            "Category": categorization["category"],
            "Priority": categorization["priority"]}
