import requests
import os
from twilio.rest import Client
import os

api_key = os.getenv("OPEN_WEATHER_API_KEY")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_VIRTUAL_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("TWILIO_VERIFIED_NUMBER")

parameters = {
    "lat": 52.52,
    "lon": 13.40,
    "appid": api_key,
    "exclude": "currently,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.raise_for_status())
print(response)
data = response.json()

weather_data = data["hourly"][:12]
# new_data = [item['weather'][0]['id'] for item in weather_data]
will_rain = False
for hour_data in weather_data:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It is going to rain",
        from_= TWILIO_VIRTUAL_NUMBER,
        to=TWILIO_VERIFIED_NUMBER
    )

    print(message.status)