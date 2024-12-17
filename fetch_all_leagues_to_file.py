import requests

# Konfiguracja API
API_URL = "https://v3.football.api-sports.io/leagues"
API_KEY = "dd0cc9e15e8937d5a1459928b80ec9b4"  # Twój klucz API
HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

def fetch_all_leagues():
    """
    Pobiera listę wszystkich lig z API Football i zapisuje ją do pliku txt.

    Zapisuje do pliku leagues.txt.
    """
    response = requests.get(API_URL, headers=HEADERS)
    if response.status_code == 200:
        leagues = response.json().get("response", [])
        with open("leagues.txt", "w", encoding="utf-8") as file:
            for league in leagues:
                league_info = (
                    f"ID: {league['league']['id']}, "
                    f"Name: {league['league']['name']}, "
                    f"Country: {league['country']['name']}\n"
                )
                file.write(league_info)
        print("Lista lig została zapisana do pliku leagues.txt")
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fetch_all_leagues()
