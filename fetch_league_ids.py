import http.client
import json

def fetch_league_ids():
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "dd0cc9e15e8937d5a1459928b80ec9b4"  # Twój klucz API
    }

    conn.request("GET", "/leagues", headers=headers)
    res = conn.getresponse()
    data = res.read()

    leagues = json.loads(data.decode("utf-8"))
    leagues_by_country = {}

    # Przetwarzanie danych
    for league in leagues.get("response", []):
        country = league["country"]["name"]
        league_name = league["league"]["name"]
        league_id = league["league"]["id"]

        if country not in leagues_by_country:
            leagues_by_country[country] = {}
        leagues_by_country[country][league_name] = league_id

    return leagues_by_country

# Zapisanie wyników do pliku JSON
if __name__ == "__main__":
    league_data = fetch_league_ids()
    with open("leagues.json", "w", encoding="utf-8") as f:
        json.dump(league_data, f, indent=4, ensure_ascii=False)
    print("League IDs have been saved to 'leagues.json'")
    