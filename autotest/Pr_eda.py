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


    def test_footer_element(self):
        for page in pages:
            resp = requests.get(base_url + page)
            assert resp.status_code == 200, f"Страница {page} недоступна"
            
            soup = BeautifulSoup(resp.content, "html.parser")
            element = soup.find("footer", class_="b-f")
            assert element is not None, f"Не удалось найти элемент <footer> с классом 'b-f' на странице {page}"

    def test_sitemap(self):
        resp = requests.get(base_url + 'sitemap.xml')
        assert resp.status_code == 200, "На сайте отсутствует sitemap"
        xml_content = resp.content
        try:
            root = ET.fromstring(xml_content)
            assert len(root) > 0, "Sitemap пустой"
            print("Sitemap не пустой")
        except ET.ParseError:
            assert False, "Некорректный формат XML"