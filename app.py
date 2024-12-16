from flask import Flask, jsonify, request, send_from_directory
import json
import requests
from datetime import date

app = Flask(__name__, static_folder="static", template_folder="templates")

API_KEY = "dd0cc9e15e8937d5a1459928b80ec9b4"
HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

# Ładowanie lig z pliku JSON
with open("leagues.json", "r", encoding="utf-8") as f:
    LEAGUES_BY_COUNTRY = json.load(f)

@app.route("/")
def home():
    return send_from_directory("templates", "index.html")

@app.route("/api/leagues", methods=["GET"])
def get_leagues():
    return jsonify(LEAGUES_BY_COUNTRY)

@app.route("/api/matches", methods=["GET"])
def get_matches():
    league_id = request.args.get("league")
    match_date = request.args.get("date", date.today().isoformat())
    season = request.args.get("season")

    if not league_id or not match_date or not season:
        missing_params = []
        if not league_id:
            missing_params.append("league")
        if not match_date:
            missing_params.append("date")
        if not season:
            missing_params.append("season")
        return jsonify({"error": f"Missing required parameters: {', '.join(missing_params)}"}), 400

    url = f"https://v3.football.api-sports.io/fixtures?league={league_id}&season={season}&date={match_date}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return jsonify(response.json().get("response", []))
    else:
        return jsonify({"error": "Failed to fetch matches", "details": response.text}), response.status_code

@app.route("/api/matches/all", methods=["GET"])
def get_all_matches():
    match_date = request.args.get("date", date.today().isoformat())
    season = request.args.get("season", date.today().year)

    url = f"https://v3.football.api-sports.io/fixtures?season={season}&date={match_date}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return jsonify(response.json().get("response", []))
    else:
        return jsonify({"error": "Failed to fetch matches", "details": response.text}), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
