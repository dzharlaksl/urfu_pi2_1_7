"""
Модуль предоставляет интерфейс для работы с моделью, которая
преобразовывает аудио в текст.
"""

import torch
import torchaudio
from transformers import pipeline
from pathlib import Path


def load_model():
    """
    Задает настройки модели и готовит ее к дальнейшему использованию.
    При использовании с интерфейсом Streamlit, функцию следует оборачивать
    в отдельную и декоратор @st.cache_resource для кэширования.

    Returns:
        Pipeline: Подготовленная модель с преднастройками
    """

    model_name = 'openai/whisper-base'
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model_name,
        device=device, generate_kwargs={
            "task": "transcribe"}
    )

    return pipe


def prepare_audio(audio):
    """
    Преобразует аудиоданные из файла в словарь, пригодный для использования в моделях.
    В качестве элементов словаря присутствуют аудиоданные в виде массив и частота.

    Args:
        audio (str or BinaryIO): Путь до файла, содержащего аудио, либо бинарные данные.

    Returns:
        dict: array - аудиоданные, sampling_rate - частота
    """

    # Преобразуем аудиофайл в данные, пригодные для моделей
    tensor, sampling_rate = torchaudio.load(audio)
    sample = {'array': tensor.numpy()[0], 'sampling_rate': sampling_rate}

    return sample


def transcribe(model, audio):
    """
    Распознает слова в аудиоданных и возвращает в форме строки.

    Args:
        audio (str or BinaryIO): Путь до файла, содержащего аудио, либо бинарные данные.

    Returns:
        str: Текст, произнесенный в аудиофайле
    """

    sample = prepare_audio(audio)    
    text = model(sample.copy(), batch_size=8)['text'].strip()
    #text = "здесь какой-то текст"

    return text


# Функция теста работопособности
if __name__ == '__main__':
    
    path_audio = Path(__file__).resolve().parent.parent / "test/sample1.flac"
    model = load_model()
    text = transcribe(model, path_audio)
    print(text)