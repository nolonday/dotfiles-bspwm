#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent().random
headers = {'user-agent' : ua}
url_dol = "https://www.banki.ru/products/currency/usd/"
req_dol = requests.get(url_dol,headers).text
soup_dol = BeautifulSoup(req_dol,'lxml')
dols = soup_dol.find('div',class_='Text__sc-j452t5-0 bCCQWi')
print(f" {dols.text}")