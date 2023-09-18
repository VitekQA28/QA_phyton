# pytest_ui_api_template

## Шаблоны для автоматизации тестирования на python

### Шаги:
1. Склонировать проект 'git clone https://'
2. Установить все зависимости
3. Запустить тесты 'pytest'


### Стэк:
- pytest
- selenium
- requests
- _sqlalchemy_
- allure
- config

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./db - хелперы для работы с БД

### Полезные ссылки:

- [Подсказка по marcdown] (https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore] (https://www.toptal.com/developers/gitignore)


### Библиотеки (!)
- pip install pytest
- pip install selenium
- pip install webdriver-manager


### Команды для теста:
1. Запуск теста  python -m pytest
2. Сгенерировать файлы теста python -m pytest --alluredir=.\allure-files
3. Сгенерировать отчет на основе файлов allure generate allure-files -o allure-report
4. Запустить отчет allure open allure-report