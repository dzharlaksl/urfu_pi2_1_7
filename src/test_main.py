import pytest

from pathlib import Path
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.mark.anyio
def test_main_sample1():
    # given
    filename = "sample1.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post("/ticket-info/",
                               files={"audio_file": (
                                   filename, content,
                                   "audio/flac")})
        # then
        assert response.status_code == 200
        assert response.json() == {
            "text": "going along slushy country roads and speaking to damp audiences in drafty "
                    "schoolrooms day after day for fortnight. He'll have to put in an appearance "
                    "at some place of worship on Sunday morning, and he can come to us "
                    "immediately afterwards.",
            "category": 0,
            "priority": 0}


@pytest.mark.anyio
def test_main_sample2():
    # given
    filename = "sample2.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post("/ticket-info/",
                               files={"audio_file": (
                                   filename, content,
                                   "audio/flac")})
        # then
        assert response.status_code == 200
        assert response.json() == {
            "text": "Добрый день. Заходу в банк лен, загружают транзакции. Ничего не грудица. "
                    "Банк не работает. Нужно срочно провести платежи. Очень важно. Пожалуйста, "
                    "как можно быстрее решить и данную проблему.",
            "category": 1,
            "priority": 1}


@pytest.mark.anyio
def test_main_sample3():
    # given
    filename = "sample3.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post("/ticket-info/",
                               files={"audio_file": (
                                   filename, content,
                                   "audio/flac")})
        # then
        assert response.status_code == 200
        assert response.json() == {
            "text": "Дорогая, у меня соединение перестало с интернетом работать. Нет доступа к "
                    "сайтам знакомств и почти нет доступа. Вообще никуда нет доступа. Что делать?",
            "category": 2,
            "priority": 0}


@pytest.mark.anyio
def test_main_sample4():
    # given
    filename = "sample4.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post("/ticket-info/",
                               files={"audio_file": (
                                   filename, content,
                                   "audio/flac")})
        # then
        assert response.status_code == 200
        assert response.json() == {
            "text": "Здравствуйте, у нас закончилась в принтере Тоннер. Пожалуйста, пришли, "
                    "кого-нибудь, чтобы поменяли Тоннер для того, чтобы мы могли распечатать "
                    "очень важные и критические документы.",
            "category": 8,
            "priority": 1}


@pytest.mark.anyio
def test_main_sample5():
    # given
    filename = "sample5.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post("/ticket-info/",
                               files={"audio_file": (
                                   filename, content,
                                   "audio/flac")})
        # then
        assert response.status_code == 200
        assert response.json() == {
            "text": "Добрый день не можем провести финансирование.",
            "category": 0,
            "priority": 0}


@pytest.mark.anyio
def test_main_sample6():
    # given
    filename = "sample6.flac"
    path_audio = Path(__file__).resolve().parent.parent / "test/" / filename
    with open(path_audio, "rb") as content:
        # when
        response = client.post("/ticket-info/",
                               files={"audio_file": (
                                   filename, content,
                                   "audio/flac")})
        # then
        assert response.status_code == 200
        assert response.json() == {
            "text": "Здравствуйте, меня виндус не загружается. Просьба решить проблему.",
            "category": 0,
            "priority": 2}
