"""
Модуль предоставляет интерфейс для работы с моделью, которая
преобразовывает аудио в текст.
"""

import torch
import torchaudio
from transformers import pipeline
from pathlib import Path


def load_model(device=None):
    """
    Задает настройки модели и готовит ее к дальнейшему использованию.
    При использовании с интерфейсом Streamlit, функцию следует оборачивать
    в отдельную и декоратор @st.cache_resource для кэширования.

    Args:
        device (str): Выбор аппартного средства для обработки, может принимать
          значения 'cuda:0' or 'cpu'. Используется для избегания проблем
          совместимости на разных платформах. Если не задан, то функция пытается
          испльзовать обработку через блоки cuda, если возможно.

    Returns:
        Pipeline: Подготовленная модель с преднастройками
    """

    model_name = 'openai/whisper-base'
    if device is None:
        device = "cuda:0" if torch.cuda.is_available() else "cpu"

    # Выводим информацию о процессе работы в консоль
    print(f'Load model to execute on device: {device}')

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model_name,
        device=device, generate_kwargs={
            "task": "transcribe"}
    )

    return pipe


def prepare_audio(audio, backend="ffmpeg"):
    """
    Преобразует аудиоданные из файла в словарь, пригодный для использования в моделях.
    В качестве элементов словаря присутствуют аудиоданные в виде массив и частота.

    Args:
        audio (str or BinaryIO): Путь до файла, содержащего аудио, либо бинарные данные.
        backend (str), default 'ffmpeg": метод декодирования аудио, может принимать значения:
         "ffmpeg", "sox", "soundfile" или None. Выбирается исходя из установленных
         приложений.

    Returns:
        dict: array - аудиоданные, sampling_rate - частота
    """

    # Преобразуем аудиофайл в данные, пригодные для моделей
    tensor, sampling_rate = torchaudio.load(audio, backend=backend)
    sample = {'array': tensor.numpy()[0], 'sampling_rate': sampling_rate}

    return sample


def transcribe(model, audio):
    """
    Распознает слова в аудиоданных и возвращает в форме строки.

    Args:

        model (pipeline): Содержит данные модель, полученную функцией load_model()
        audio (str or BinaryIO): Путь до файла, содержащего аудио, либо бинарные данные.

    Returns:
        str: Текст, произнесенный в аудиофайле
    """

    sample = prepare_audio(audio)

    text = model(sample.copy(), batch_size=8)['text'].strip()

    return text


# Функция теста работопособности
if __name__ == '__main__':

    path_audio = Path(__file__).resolve().parent.parent / "test/sample1.flac"
    model = load_model()
    text = transcribe(model, path_audio)

    print(text)
