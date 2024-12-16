from flask import Flask, jsonify, render_template, request
import json
import requests

app = Flask(__name__)

# Wczytanie pliku leagues.json
with open('leagues.json', encoding='utf-8') as f:
    LEAGUES_BY_COUNTRY = json.load(f)

API_KEY = "dd0cc9e15e8937d5a1459928b80ec9b4"
API_URL = "https://v3.football.api-sports.io"

# Pobierz ligi
@app.route('/api/leagues', methods=['GET'])
def get_leagues():
    leagues = []
    for country, leagues_data in LEAGUES_BY_COUNTRY.items():
        leagues.append({
            "country": country,
            "leagues": [{"name": league, "id": league_id} for league, league_id in leagues_data.items()]
        })
    return jsonify(leagues)

# Pobierz mecze
@app.route('/api/matches', methods=['GET'])
def get_matches():
    league_id = request.args.get("league")
    if not league_id:
        return jsonify({"error": "Brak ID ligi"}), 400
    
    url = f"{API_URL}/fixtures?league={league_id}&season=2024"
    headers = {
        "x-rapidapi-host": "v3.football.api-sports.io",
        "x-rapidapi-key": API_KEY
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "Błąd w zapytaniu do API"}), response.status_code
    
    fixtures = response.json().get("response", [])
    matches = [{
        "kick_off": fixture["fixture"]["date"],
        "league_id": league_id,
        "league_name": fixture["league"]["name"],
        "home_team": fixture["teams"]["home"]["name"],
        "away_team": fixture["teams"]["away"]["name"],
        "status": fixture["fixture"]["status"]["short"]
    } for fixture in fixtures]

    return jsonify(matches)

# Główna strona
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
