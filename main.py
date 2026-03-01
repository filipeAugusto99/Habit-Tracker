import requests
from datetime import datetime


USERNAME = "filipeaug26"
TOKEN = "sacasalkdsamcsldmcslkdm234324"
GRAPH_ID = "graph2"


pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2026, month=2, day=18)


pixel_graph_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5",
}


response = requests.post(url=pixel_graph_endpoint, json=pixel_graph_config, headers=headers)
print(response.text)