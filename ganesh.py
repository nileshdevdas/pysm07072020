import requests
from bs4 import BeautifulSoup

mypage = requests.get(
    "https://www.amazon.in/Casio-CTX700-Sensitive-Portable-Keyboard/dp/B0794RNK5V/ref=sr_1_1_sspa?dchild=1&keywords=yamaha+keyboard&qid=1594805793&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVzAzTTNIS1FIMEdUJmVuY3J5cHRlZElkPUEwNDE3OTY2MUhTNUlYWkNFVjJRRCZlbmNyeXB0ZWRBZElkPUEwODQ5MzcwMzc1TloxUTlITlFIMyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=", headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
soup = BeautifulSoup(markup=mypage.text, features="html.parser")
# print(soup)
price = soup.find("span", {'id': 'priceblock_ourprice'})
print(price.text)