import requests

url = "http://127.0.0.1:5000/api/matches"
params = {
    "league": 188,
    "season": 2024,
    "date": "2024-12-15"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Status Code:", response.status_code)
    print("Response JSON:")
    print(response.json())
else:
    print("Error:", response.status_code)
    print(response.text)
