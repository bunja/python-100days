import requests
from bs4 import BeautifulSoup
import locale
import smtplib
import os

URL = "https://www.amazon.de/-/en/New-Apple-iPhone-12-Pro/dp/B08L5VCMVF/ref=sr_1_5?dchild=1&keywords=iphone%2B12&qid=1621370783&sr=8-5&th=1"

header = {
    "Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

response = requests.get(url=URL, headers=header)
website_html = response.text

soup = BeautifulSoup(website_html, "lxml")
price = soup.find(name="span", id="priceblock_ourprice")
title = soup.find(name="span", id="productTitle").text.strip()
price_no_curr = price.text[1:]
locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
price_as_loc = locale.atof(price_no_curr)


print(price_as_loc)
print(title)

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD_SMTPLIB")
to_email = os.getenv("TO_EMAIL")
if price_as_loc < 1500:
    msg = f"Subject: Amazon Price ALert!\n\n {title} now {price_as_loc}$\n\n {URL}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=msg)



