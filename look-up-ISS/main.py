import requests
from datetime import datetime
import math
import smtplib
import time
import os

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD_SMTPLIB")
to_email = os.getenv("TO_EMAIL")


MY_LAT = 52.520008
MY_LNG = 13.404954





def is_over_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print(iss_position)
    x = (latitude - MY_LAT)**2
    y = (longitude - MY_LNG)**2
    d = math.sqrt(x + y)
    if d <= 5:
        return True
    else:
        return False

def is_seen():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    # print(sunrise.split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = datetime.now().hour

    print(time_now)
    if sunset <= time_now <= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if is_seen() and is_over_me():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to_email,
                                msg=f"Subject:Hello, darling!\n\n Hey? look up")



