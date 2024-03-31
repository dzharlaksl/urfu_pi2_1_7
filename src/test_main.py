import pytest

from pathlib import Path
from fastapi.testclient import TestClient
from main import app
from tools_for_test import cosine_similarity

client = TestClient(app)


@pytest.mark.anyio
def test_main_sample1():
    # given
    filename = "sample1.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post(
            "/ticket-info/", files={"audio_file": (filename, content, "audio/flac")}
        )
        # then
        assert response.status_code == 200

        reference_text = (
            "Going along slushy country roads and speaking to damp audiences in drafty "
            "schoolrooms day after day for fortnight. He'll have to put in an appearance "
            "at some place of worship on Sunday morning, and he can come to us "
            "immediately afterwards."
        )

        result = response.json()
        assert cosine_similarity(result["text"], reference_text) >= 0.9
        assert result["category"] == 0
        assert result["priority"] == 0


@pytest.mark.anyio
def test_main_sample2():
    # given
    filename = "sample2.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post(
            "/ticket-info/", files={"audio_file": (filename, content, "audio/flac")}
        )
        # then
        assert response.status_code == 200

        reference_text = (
            "Добрый день. Захожу в банк-клиент, загружаю транзакции. Ничего не грузится. "
            "Банк не работает. Нужно срочно провести платежи. Очень важно, пожалуйста, "
            "как можно быстрее решите и данную проблему."
        )

        result = response.json()
        assert cosine_similarity(result["text"], reference_text) >= 0.9
        assert result["category"] == 1
        assert result["priority"] == 1


@pytest.mark.anyio
def test_main_sample3():
    # given
    filename = "sample3.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post(
            "/ticket-info/", files={"audio_file": (filename, content, "audio/flac")}
        )
        # then
        assert response.status_code == 200

        reference_text = (
            "Здравствуйте, у меня соединение перестало с интернетом работать. Нет доступа к "
            "сайтам знакомств, к почте нет доступа. Вообще никуда нет доступа. Что делать?"
        )

        result = response.json()
        assert cosine_similarity(result["text"], reference_text) >= 0.9
        assert result["category"] == 2
        assert result["priority"] == 0


@pytest.mark.anyio
def test_main_sample4():
    # given
    filename = "sample4.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post(
            "/ticket-info/", files={"audio_file": (filename, content, "audio/flac")}
        )
        # then
        assert response.status_code == 200

        reference_text = (
            "Здравствуйте, у нас закончился в принтере тоннер. Пожалуйста, пришлите, "
            "кого-нибудь, чтобы поменяли тоннер для того, чтобы мы могли распечатать "
            "очень важные, критические документы."
        )

        result = response.json()
        assert cosine_similarity(result["text"], reference_text) >= 0.9
        assert result["category"] == 8
        assert result["priority"] == 1


@pytest.mark.anyio
def test_main_sample6():
    # given
    filename = "sample6.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post(
            "/ticket-info/", files={"audio_file": (filename, content, "audio/flac")}
        )
        # then
        assert response.status_code == 200

        reference_text = (
            "Здравствуйте, меня windows не загружается. Просьба решить проблему."
        )

        result = response.json()
        assert cosine_similarity(result["text"], reference_text) >= 0.9
        assert result["category"] == 0
        assert result["priority"] == 2
