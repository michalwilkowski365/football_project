import http.client
import json

def fetch_seasons():
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "dd0cc9e15e8937d5a1459928b80ec9b4"  # Twój klucz API
    }

    conn.request("GET", "/leagues/seasons", headers=headers)
    res = conn.getresponse()
    data = res.read()

    # Parsowanie JSON
    seasons = json.loads(data.decode("utf-8"))
    return seasons

if __name__ == "__main__":
    # Pobierz dostępne sezony
    seasons_data = fetch_seasons()

    # Wyświetl dostępne sezony
    print("Available seasons:")
    print(json.dumps(seasons_data, indent=4, ensure_ascii=False))
