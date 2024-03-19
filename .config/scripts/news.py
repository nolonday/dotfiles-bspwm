#!/usr/bin/python3

#imporst
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

#declaration of variables
ua = UserAgent().random
headers = {"user-agent": ua}
url = "https://ria.ru/world/"
url1 = "https://gtrksmolensk.ru/news/"
#search html tegs 
req = requests.get(url,headers).text
soup = BeautifulSoup(req,'lxml') 
div = soup.find_all('div',class_='list-item')
print("  Новости в мире ")
print("---------------------------------------------------------------------------------------")
for d in div:
    name = d.find('a',class_='list-item__title color-font-hover-only')
    print(f" {name.text}")
    print(f"󰴜 {name.get('href')}")
    time = d.find('div',class_='list-item__date')
    print(f"󱑇 {time.text}")
    print()
print("---------------------------------------------------------------------------------------")
print("  Новости в Смоленской области ")
print("---------------------------------------------------------------------------------------")
#search html tegs 
req1 = requests.get(url1,headers).text
soup1 = BeautifulSoup(req1,'lxml')
article = soup1.find_all('article',class_='news-preview news-preview--general')
for ar in article:
    name = ar.find('h1',class_='news-preview__header-text')
    print(f" {name.text}")
    disc = ar.find('div',class_='news-preview__content').find('p')
    print(f" {disc.text.strip()}")
    time = ar.find('time',class_='news-info-short__time')
    print(f"󱑇 {time.text.strip()}")
    print()
print("---------------------------------------------------------------------------------------")
input()
