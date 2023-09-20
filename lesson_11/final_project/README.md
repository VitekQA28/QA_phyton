# pytest_ui_api_template

## Шаблоны для автоматизации тестирования на python

### Шаги

1. Склонировать проект (git clone https://)
2. Установить все зависимости
  a. Для опредения зависимостей выполняется комманда (python -m pip freeze > requirements.txt)
  b. Для автоматической установки зависимостей выполняется комманда (python -m pip install -r requirements.txt)
3. Запустить тесты (pytest)
4. Cгенерировать файлы для отчета (python -m pytest --alluredir=.\allure-files)
5. Cгенерировать отчет (allure generate allure-files -o allure-report)
6. Открыть отчет в браузере (allure open allure-report)

### Стэк

- pytest
- selenium
- webdriver-manager
- requests
- _sqlalchemy_
- allure
- configparser
- json

### Структура

- ./auto - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД
- ./configuration - провайдер настроек
  - test_config.ini - настройки для тестов
- ./testdata - провайдер тестовых данных
  - test_data.json

### Полезные ссылки

- [Подсказка по marcdown] (<https://www.markdownguide.org/cheat-sheet/>)
- [Генератор файла .gitignore] (<https://www.toptal.com/developers/gitignore>)
- [Установка аллюр на ПК] (<https://docs.qameta.io/allure-report/>)
- [Документация pip freeze] (<https://pip.pypa.io/en/stable/cli/pip_freeze/>)

### Команды для теста

1. Запуск всех тестов (python -m pytest)
2. Запуск только ui тестов (python -m pytest -m ui)
3. Запуск только api тестов (python -m pytest -m api)
4. Сгенерировать файлы теста python (-m pytest --alluredir=.\allure-files)
5. Сгенерировать отчет на основе файлов (allure generate allure-files -o allure-report)
6. Запустить отчет (allure open allure-report)
