# pytest_ui_api_template

## Шаблоны для автоматизации тестирования на python

### Шаги

1. Склонировать проект (git clone https://)
2. Установить все зависимости
3. Запустить тесты (pytest)
4. Cгенерировать файлы для отчета (python -m pytest --alluredir=.\allure-files)
5. Cгенерировать отчет (allure generate allure-files -o allure-report)
6. Открыть отчет в браузере (allure open allure-report)

### Стэк

- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

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

- [Подсказка по marcdown] (https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore] (https://www.toptal.com/developers/gitignore)
- [Установка аллюр на ПК] (https://docs.qameta.io/allure-report/)

### Библиотеки (!)

- pip install pytest
- pip install selenium
- pip install webdriver-manager
- pip install allure-pytest
- pip install requests

### Команды для теста

1. Запуск всех тестов (python -m pytest)
2. Запуск только ui тестов (python -m pytest -m ui)
3. Запуск только api тестов (python -m pytest -m api)
4. Сгенерировать файлы теста python (-m pytest --alluredir=.\allure-files)
5. Сгенерировать отчет на основе файлов (allure generate allure-files -o allure-report)
6. Запустить отчет (allure open allure-report)
