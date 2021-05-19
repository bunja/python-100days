import requests
from twilio.rest import Client
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

API_STOCK_KEY = os.getenv("API_STOCK_KEY")

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": API_STOCK_KEY
}

response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
cleaned_data = data['Time Series (Daily)']

# first2pairs = {k: cleaned_data[k] for k in list(cleaned_data.keys())[:2]}
first_two_pairs = [value for (key, value) in list(cleaned_data.items())[:2]]
yesterday_close = float(first_two_pairs[0]['4. close'])
day_before_close = float(first_two_pairs[1]['4. close'])
difference = abs(day_before_close - yesterday_close)
percentage = difference / day_before_close

if percentage >= 0.0005:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get("https://newsapi.org/v2/everything", news_params)
    news_response.raise_for_status()

    articles = news_response.json()['articles'][:3]

    formated_articles = [f"Headline: {a['title']}.\nBrief: {a['description']}" for a in articles]
    print(formated_articles)
    for item in formated_articles:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body= item,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

        print(message.status)
