from bs4 import BeautifulSoup
import requests

header = {
    "Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56945647192383%2C%22east%22%3A-122.29720152807617%2C%22south%22%3A37.665033606806276%2C%22north%22%3A37.88538511109396%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
response = requests.get(url=URL, headers=header)

zillow_page = response.text
soup = BeautifulSoup(zillow_page, "html.parser")
listings = soup.select("article.list-card")
data_list = []
for listing in listings:
    if listing.a is None:
        continue
    url = listing.a['href']
    if not url.startswith('https'):
        url = "https://www.zillow.com" + url
        
    address = listing.a.address.text
    price = listing.select('.list-card-price')[0].text.split()[0].split('/')[0]
    
    a = {
        "address": address,
        "price": price,
        "url": url,
    }
    data_list.append(a)

print(data_list)

