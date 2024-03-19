#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent().random
headers = {'user-agent' : ua}
url_eur = "https://www.banki.ru/products/currency/eur/"

req_eur = requests.get(url_eur,headers).text
soup_eur = BeautifulSoup(req_eur,'lxml')
eur = soup_eur.find('div',class_='Text__sc-j452t5-0 bCCQWi')
print(f" {eur.text}")
