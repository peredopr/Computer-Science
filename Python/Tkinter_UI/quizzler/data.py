import requests

parameters = {
    "amount": 20,
    "type": "boolean",
    "category": 9
}

response = requests.get(url="https://opentdb.com/api.php?amount=20&category=9&type=boolean", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]