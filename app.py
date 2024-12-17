from flask import Flask, jsonify, request, send_from_directory
import requests
from datetime import date
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__, static_folder="static", template_folder="templates")

# Klucz API
API_KEY = "dd0cc9e15e8937d5a1459928b80ec9b4"
HEADERS = {
    "x-rapidapi-host": "v3.football.api-sports.io",
    "x-rapidapi-key": API_KEY
}

# Dokładna lista lig (Twoja lista, nie zmieniam jej)
LEAGUES = [
    4, 21, 61, 144, 71, 39, 78, 135, 88, 94, 140, 179, 180, 1, 803, 62, 2, 186,
    333, 301, 202, 203, 204, 206, 66, 65, 233, 329, 199, 198, 197, 79, 80, 529,
    81, 7, 8, 129, 188, 191, 193, 220, 219, 218, 110, 119, 120, 271, 305, 40,
    46, 45, 47, 48, 43, 41, 42, 15, 480, 72, 253, 257, 296, 551, 244, 526, 481,
    102, 101, 98, 99, 100, 121, 528, 3, 807, 547, 128, 183, 6, 9, 255, 550, 555,
    556, 563, 564, 368, 315, 96, 16, 17, 25, 141, 136, 103, 89, 95, 113, 137,
    200, 207, 210, 239, 73, 90, 145, 189, 146, 82, 139, 91, 142, 130, 190, 165,
    114, 208, 262, 263, 259, 286, 292, 293, 307, 308, 14, 18, 20, 38, 490, 106,
    5, 323, 324, 107, 332, 345, 346, 808, 143, 321, 31, 32, 33, 34, 29, 30, 942,
    943, 49, 493, 537, 50, 51, 109, 83, 84, 85, 86, 87, 435, 436, 437, 438, 484,
    518, 525, 147, 167, 12, 13, 209, 115, 181, 97, 108, 105, 347, 35, 254, 192,
    194, 195, 196, 648, 695, 696, 702, 703
]

# Pobieranie meczów dla danej ligi
def fetch_matches(league_id, date_param):
    response = requests.get(
        "https://v3.football.api-sports.io/fixtures",
        headers=HEADERS,
        params={"league": league_id, "season": "2024", "date": date_param}
    )
    if response.status_code == 200:
        return response.json().get("response", [])
    return []

@app.route("/")
def home():
    return send_from_directory(app.template_folder, "index.html")

@app.route("/api/matches", methods=["GET"])
def get_matches():
    date_param = request.args.get("date", date.today().isoformat())
    matches = []

    with ThreadPoolExecutor() as executor:
        results = executor.map(lambda league: fetch_matches(league, date_param), LEAGUES)
        for result in results:
            matches.extend(result)

    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
