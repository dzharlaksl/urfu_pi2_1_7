from pathlib import Path
from transcribe import load_model, transcribe


def test_transcribe_sample1():
    # given
    path_audio = Path(__file__).resolve().parent.parent / "test/sample1.flac"
    # when
    model = load_model()
    text = transcribe(model, path_audio)
    # when
    assert text == ("going along slushy country roads and speaking to damp audiences in drafty "
                    "schoolrooms day after day for fortnight. He'll have to put in an appearance "
                    "at some place of worship on Sunday morning, and he can come to us "
                    "immediately afterwards.")


def test_transcribe_sample2():
    # given
    path_audio = Path(__file__).resolve().parent.parent / "test/sample2.flac"
    # when
    model = load_model()
    text = transcribe(model, path_audio)
    # when
    assert text == ("Добрый день. Заходу в банк лен, загружают транзакции. Ничего не грудица. Банк "
                    "не работает. Нужно срочно провести платежи. Очень важно. Пожалуйста, "
                    "как можно быстрее решить и данную проблему.")


def test_transcribe_sample3():
    # given
    path_audio = Path(__file__).resolve().parent.parent / "test/sample3.flac"
    # when
    model = load_model()
    text = transcribe(model, path_audio)
    # when
    assert text == ("Дорогая, у меня соединение перестало с интернетом работать. Нет доступа к "
                    "сайтам знакомств и почти нет доступа. Вообще никуда нет доступа. Что делать?")


def test_transcribe_sample4():
    # given
    path_audio = Path(__file__).resolve().parent.parent / "test/sample4.flac"
    # when
    model = load_model()
    text = transcribe(model, path_audio)
    # when
    assert text == ("Здравствуйте, у нас закончилась в принтере Тоннер. Пожалуйста, пришли, "
                    "кого-нибудь, чтобы поменяли Тоннер для того, чтобы мы могли распечатать "
                    "очень важные и критические документы.")


def test_transcribe_sample5():
    # given
    path_audio = Path(__file__).resolve().parent.parent / "test/sample5.flac"
    # when
    model = load_model()
    text = transcribe(model, path_audio)
    # when
    assert text == "Добрый день не можем провести финансирование."


def test_transcribe_sample6():
    # given
    path_audio = Path(__file__).resolve().parent.parent / "test/sample6.flac"
    # when
    model = load_model()
    text = transcribe(model, path_audio)
    # when
    assert text == "Здравствуйте, меня виндус не загружается. Просьба решить проблему."
