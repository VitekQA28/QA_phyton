import requests
import pytest
from bs4 import BeautifulSoup
import urllib.robotparser
import xml.etree.ElementTree as ET
from Pr_eda import Pr_eda

'''
1) rodots - закрыт сайт или нет от индексации, проверить все варианты
2) все страницы сайта открываются +
3) Проверка наличия мета-тегов в HTML-коде страницы: +
    1 - title
    2 - keywords
    3 - description
4) Проверка наличия определенного элемента на странице, например footer сайта. +
5) есть ли на сайте sitemap и не пустой ли он +
'''

def test_robots(): #rodots - закрыт сайт или нет от индексации, проверить все варианты
    test_website = Pr_eda()
    test_website.test_robots()
   
def test_status_page(): #все страницы сайта открываются
    test_website = Pr_eda()
    test_website.test_status_page()

def test_check_meta_tags(): #Проверка наличия мета-тегов в HTML-коде страницы
    test_website = Pr_eda()
    test_website.check_meta_tags()

def test_footer_element(): #Проверка наличия определенного элемента на странице, например footer сайта
    test_website = Pr_eda()
    test_website.footer_element()

def test_sitemap(): #есть ли на сайте sitemap и не пустой ли он
    test_website = Pr_eda()
    test_website.test_sitemap()

