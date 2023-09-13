import requests
from bs4 import BeautifulSoup
import urllib.robotparser
import xml.etree.ElementTree as ET

base_url = 'https://prostayaeda.s2.citruspro.ru/'

pages = [
    'catalog', 
    'delivery', 
    'stocks', 
    'about', 
    'contacts',
    'vacancies', 
    'legal-info', 
    'personal', 
    'order'
]

class Pr_eda:
    def __init__(self):
        self.index = urllib.robotparser.RobotFileParser()
        self.index.set_url(base_url + "robots.txt")
        self.index.read()

    def test_robots(self):
        assert self.index.can_fetch("*", base_url), 'Сайт закрыт от индексации'

    def test_status_page(self):
        for page in pages:
            resp = requests.get(base_url + page)
            assert resp.status_code == 200, f"Страница {page} недоступна"

    def test_meta_tags(self):
        checked_pages = [] # Создаем список для отслеживания протестированных страниц
        for page in pages:
            resp = requests.get(base_url + page)
            assert resp.status_code == 200, f"Страница {page} недоступна"
            
            soup = BeautifulSoup(resp.content, "html.parser")
            attributes = ["title", "keywords", "description"]
            
            for attribute in attributes:
                element = soup.find("meta", {"name": attribute})
                assert element is not None, f"Не удалось найти элемент <meta> с атрибутом name='{attribute}' на странице {page}"
                content = element.get("content")
                assert content != "", f"Атрибут 'content' элемента <meta> с атрибутом name='{attribute}' пустой на странице {page}"
            checked_pages.append(page)  # Добавляем протестированную страницу в список
        assert len(checked_pages) != len(pages), f"Не все страницы были протестированы. Не протестированные страницы: {set(pages) - set(checked_pages)}"

# Создаем экземпляр класса и запускаем тесты
pr_eda = Pr_eda()
pr_eda.test_robots()
pr_eda.test_status_page()
pr_eda.test_meta_tags()
