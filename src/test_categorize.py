from categorize import words_from_text, categorize_text, determine_priority, ticket_info


def test_returns_normalized_words():
    # Given
    text = "Привет! Это тестовое предложение для проверки функции."

    # When
    result = words_from_text(text)

    # Then
    expected_result = ['привет', 'это', 'тестовый', 'предложение', 'для', 'проверка', 'функция']
    assert result == expected_result


def test_words_form_text_empty_input_text():
    # Given
    text = ""

    # When
    result = words_from_text(text)

    # Then
    expected_result = []
    assert result == expected_result


def test_categorize_text():
    # Given
    text = ("Привет! Меня интересуют инвестиции. Ваш банк кажется мне лучшим кандидатом для моего "
            "депозита.")

    # When
    category = categorize_text(text)

    # Then
    assert category == 1


def test_short_text_categorization():
    # Given
    text = "Я"

    # When
    category = categorize_text(text)

    # Then
    assert category == 0


def test_determine_priority_high_importance():
    # Given
    text = "Добрый день! Помогите мне срочно! У меня неотложная задача!"

    # When
    priority = determine_priority(text)

    # Then
    assert priority == 1


def test_determine_priority_empty_text():
    # Given
    text = ""

    # When
    priority = determine_priority(text)

    # Then
    assert priority == 0


def test_correct_category_and_priority():
    # Given
    text = "Привет! Это обычный запрос в поддержку по поводу установки обновлений Linux."

    # When
    result = ticket_info(text)

    # Then
    assert result["category"] == 7
    assert result["priority"] == 3


def test_empty_text_category_and_priority():
    # Given
    text = ""

    # When
    result = ticket_info(text)

    # Then
    assert result == {'category': 0, 'priority': 0}
