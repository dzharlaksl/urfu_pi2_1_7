# Тикет-система для служб техподдержки (MVP)

---

## 1. Цель проекта
__Цель проекта__ - реализация функционала, который позволит изменить и оптимизировать бизнес-процесс заказчика (служба технической поддержки) на обслуживание пользователей. Предполагается снижение издержек служб технической поддержки по приему заявок пользователей, за счет экономии на сотрудниках колл-центра, осуществляющих первичную приемку звоноков и внесение заявок в тикет-систему.
Сервис решает следующие __задачи__:
- получение информации от пользователя о возникшем инцеденте по телефону 24/7
- транскрибация аудио-записи в текст
- определение по контексту типа проблемы (категории) с которой обратился пользователь- 
- определение приоритета задачи

---

## 2. Функционал сервиса
__Сервис__ реализован в виде набора python-скриптов которые можно легко интегрировать в существующую тикет-систему заказчика (службы тех.поддержки), а также в виде backend модуля с API. Это позволяет, в зависимости от требований заказчика к хранению и обработке данных, как реализовать возможность интегрирации функционала локально, так и по API запросу к удаленному серверу, на котором будет подтянт uvicorn сервер с fastapi.

---

## 3. Бизнес проблематика
Компания осуществляет услуги по тех.поддержке (сеть, безопасность, работа ОС, офисного ПО, обслуживание техики и тп). Есть желание снизить расходы на сотрудников принимающих телефонные обращения пользователей, с последюущим описанием и ручной постановкой задачи исполнителю в тикет-систему (указанием категории проблемы, приоритета).

---

## 4. Текущий бизнес-процесс
Пользователи звонят на линию поддержки, рассказывают о возникшей проблеме, после чего специалист колл-центра создает задачу на исполнителя в зависимости от специфики задачи и уровня необходимых компетенций.

---

## 5. Целевой бизнес-процесс 
- выделяется отдельная телефонная линия для приема звонков пользователей (в режиме 24/7)
- при соединении включается воспроизведение приветствия, а также просьба описать проблему. Например: «Здравствуйте. Вы позвонили в службу поддержки. Пожалуйста, расскажите о возникшей проблеме. Оно будет записано и назначено не исполнение сотруднику поддержки».
- автоотвечтик записывает звонок
- аудиофайл направляется на распознавание и перевод в текст с помощью модели ИИ
- модель переводит аудио в текст
- далее по тексту определяется категория задачи и ее приоритет с помощью подобия Жаккара
- тикет-система заказчика получает текст обращения, категорию, приоритет и создает тикет на исполнителя, обладающего необходимой квалификацией

---

## 6. Запуск приложения
Разрабатываемый сервис представляет собой backend с API-методами для обработки заявок. 
Ознакомиться c fastapi документацией можно по ссылке: http://80.234.33.45:8008/docs
Предполагается, что fronend`ом является тикет-система службы поддержки, которая использует методы предалагаемого нами сервиса.
Однако для демонстрации возможностей backend был реализован веб-интерфейс на streamlit: http://80.234.33.45:8501/

Для локального запуска проекта необходимо скачать исходный код проекта и настроить виртуальное окружение. 
Это можно сделать следующей командой:
```bash
python3 -m venv namedir
```
После установки виртуального окружения необходимо его активировать
- команда для linux:
```bash
source namedir/bin/activate
```
- команда для windows:
```
.\scripts\activate.ps1
```
И далее установить в активированную виртуальную среду список необходимых библиотек для работы приложения. 
Все необходимые бибилиотеки указаны в requirements.txt. Для массовой установки бибилиотек достаточно использовать команду:
```bash
pip install -r requirements.txt
```
Для запуска приложения используйте команду в директории проекта:
```bash
streamlit run frontend.py
```
Для запуска backend севрера с API используйте команду:
```bash
uvicorn main:app --port 8008
```

**Используемые технологии, инструменты, алгоритмы:**
`Python`, `ffmpeg`, `Whisper`, `Streamlit`, `uvicorn`, `fastAPI` 

---

## 7. Команда
Команда состоит из 6-х человек (группа №7):
- [Игорь Ерошин](https://github.com/tmerurfu)
- [Татьяна Меркурьева](https://github.com/dzharlaksl)
- [Евгений Брылин](https://github.com/bev141)
- [Олег Перевиспа](https://github.com/operevispa)
- [Вадим Монахов](https://github.com/MonakhovVadim)
- [Клим Колчин](https://github.com/synrocka)

---

## Лицензия
[Стандартная общественная лицензия GNU (GPL) версии 3](./gpl-3.0.txt) или выше.
