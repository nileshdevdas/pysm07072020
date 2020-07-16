import requests
from bs4 import BeautifulSoup
#
# mypage = requests.get('https://www.flipkart.com/casio-ks43-cbc600-black-ct-x700-carry-case-digital-portable-keyboard/p/itmfdf9ybgmsqgq5?pid=MKDFDF9YHKGTYVE4&marketplace=FLIPKART')
# soup = BeautifulSoup(markup=mypage.text , features="html.parser")
# price = soup.find("div", {'class': '_1vC4OE _3qQ9m1'})
# print(price.text)
#
#
awspage = requests.get(url='https://www.amazon.in/Casio-CT-X870IN-61-Key-Portable-Keyboard/dp/B07GJSCK6N/ref=sr_1_9?crid=1PJW1MOFSJM9G&dchild=1&keywords=casio+piano+keyboard&qid=1594804872&sprefix=Casio+%2Caps%2C320&sr=8-9',
headers={
        'user-agent' :
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
})
soup = BeautifulSoup(awspage.text, features="html.parser")
aws_price = soup.find("span" , {'id' : 'priceblock_ourprice1'})
print(aws_price)
if aws_price:
    print(aws_price.text)
