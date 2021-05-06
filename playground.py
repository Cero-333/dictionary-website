import requests

endpoint = "https://api.dictionaryapi.dev/api/v2/entries/en_US"

response = requests.get(f"{endpoint}/water bottle")
data = response.json()
print(data)
