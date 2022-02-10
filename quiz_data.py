import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 9,
    "difficulty":"easy"
}

response = requests.get(url="https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean", params=parameters)
question_data = response.json()["results"]


 