# urfu_pi2_1_7
URFU - second term group - Pi project - group 1.7 (Voicemail-to-ticket)

Описание проекта-задачи: расшифровка сообщений с автоответчика и создание заявок на основе сообщения. 

  Приоритизация по следующим парметрам:
  High (1) - финасовая система, сеть
  Middle (2) - почта, связь, факс
  Low (3) - ОС, принтеры

Задачи 1й спринт, каждый создает ветку и в ней папку и работает со своей частью в ней далее в субботу проверяем и делаем совмещение: 
  1) Аудио в текст (функция с использованием модели из первого проекта)
  2) Из текста в заявку (классификация по ключевым словам и приоритет) - Игорь Ерошин
  3) Программный интерфейс Fast API - Клим Колчин
  4) Пользовательский интерфейс Streamlit (ввод и загрузка аудио-файла)
  5) Пользовательский интерфейс Streamlit (вывод результата, на исновании ответа API (json файл) - вывети на экран заявку с указанным приоритетом, и кнопками "в работе\готово")
  6) Тесты на pytest
