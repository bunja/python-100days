import requests
from datetime import datetime
import os

USERNAME = os.getenv("PIX_USERNAME")
TOKEN = os.getenv("PIX_TOKEN")
GRAPH_ID = os.getenv("PIX_GRAPH_ID")


pixela_endpoint = "https://pixe.la/v1/users"
# setting up a new account on pixe.la
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# success

# -----Creating a graph endpoint--------#
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# --------Creating a pixel ---------#
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

yesterday = datetime(year=2021, month=5, day=5)

pixel_data = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "6.5",
}

# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
#
# print(response.text)

# ----------Updating pixel's quantity-------#
today = datetime.now().strftime("%Y%m%d")
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

update_data = {
    "quantity": "12.5",
}

# response = requests.put(pixel_update_endpoint, json=update_data, headers=headers)
# print(response.text)

# -----------Deleting pixel----------#
response = requests.delete(pixel_update_endpoint, headers=headers)
print(response.text)






