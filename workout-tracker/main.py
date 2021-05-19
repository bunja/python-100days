import requests
from datetime import datetime
import os

APP_ID = os.getenv("NUTR_APP_ID")
API_KEY = os.getenv("NUTR_API_KEY")

exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.getenv("SHEET_WORKOUT_ENDPOINT")
TOKEN = os.getenv("SHEET_TOKEN")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

sheet_headers = {
    "Authorization": TOKEN
}
exercise_text = input("Tell me which exercises you did: ")
parameters = {
     "query": exercise_text,
     "gender": "female",
     "weight_kg": 72.5,
     "height_cm": 167.64,
     "age": 30,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")



for exercise in result['exercises']:
    body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    print(body)

    sheety_response = requests.post(url=sheet_endpoint, json=body, headers=sheet_headers)
    print(sheety_response.text)
