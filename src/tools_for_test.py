"""
Модуль предоставляет инструменты для тестирования средствами pytest.
"""

import torch
from categorize import words_from_text


def cosine_similarity(text1, text2):
    """
    Рассчитывает косинусное расстояние между векторами,
    которое является средством оценки схожести текста.

    Args:
        text1, text2 (str): Тексты для сравнения

    Returns:
        float: оценка схожести текстов, находится в диапазоне [0;1]
    """

    # Получаем слова из текста без пунктуации, приведенные к
    # нормальной форме
    text1 = words_from_text(text1)
    text2 = words_from_text(text2)

    # Для дальнейшей обработки, необходимо токенизировать все слова.
    # Т.к. тенсоры pytorch работают с числовыми векторами, то необходимо
    # преобразовать все слова к числовым идентификаторам.
    tokens = {}
    tokens[""] = 0
    id_word = 1
    for word in set(text1 + text2):
        tokens[word] = id_word
        id_word += 1

    # Для реализации произведения векторов необходимо, чтобы векторы
    # имели одинаковую длину.
    tensor_len = max(len(text1), len(text2))
    if len(text1) < tensor_len:
        text1 = text1 + [""] * (tensor_len - len(text1))
    if len(text2) < tensor_len:
        text2 = text2 + [""] * (tensor_len - len(text2))

    # Несмотря на токены типа int, нормы вектора вычисляются только с типом float
    text1 = torch.tensor([tokens[word] for word in text1], dtype=torch.float)
    text2 = torch.tensor([tokens[word] for word in text2], dtype=torch.float)

    # Вычисляем произведение векторов
    dot_product = torch.matmul(text1, text2)

    # Вычисляем нормы векторов для последующей стандартизации
    norm1 = torch.norm(text1, dim=0, dtype=torch.float)
    norm2 = torch.norm(text2, dim=0, dtype=torch.float)

    # Определяем косинусное расстояние с приведением в интервал [0;1]
    cosine_similarity = dot_product / (norm1 * norm2)

    # До этого мы работали с тензорами, но на выходе удобнее возвращать число
    return cosine_similarity.item()
