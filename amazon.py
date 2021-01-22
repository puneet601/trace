import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Kpop-Merch-S-BE-Delux/dp/B08KD2GXK7/ref=sr_1_11?crid=2W9JYNOHIGLF4&dchild=1&keywords=bts+be+album&qid=1611320759&sprefix=BTS+BE+%2Caps%2C313&sr=8-11'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
def check_price():
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print(price)
    price=price.replace(',','.')
    converted_price = float(price[1:5])

    print(converted_price)
    if (converted_price > 5):
        send_email()
def send_email():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('puneetkaurjattana@gmail.com', 'dlswixueojrofakf')
    subject = "Price fell down!"
    body = "BUY BE ALBUM. CHECK 'https://www.amazon.in/Kpop-Merch-S-BE-Delux/dp/B08KD2GXK7/ref=sr_1_11?crid=2W9JYNOHIGLF4&dchild=1&keywords=bts+be+album&qid=1611320759&sprefix=BTS+BE+%2Caps%2C313&sr=8-11'"
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'puneetkaurjattana@gmail.com',
        'puneet1210.cse18@chitkara.edu.in',
        msg
    )
    print("Email Has BEEN SENT")
    server.quit()
    
while (True):
    check_price()
    time.sleep(60 * 60 * 24)