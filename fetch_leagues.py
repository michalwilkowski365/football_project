from api_client import APIClient

def fetch_leagues(league_ids):
    """
    Pobiera informacje o ligach na podstawie ich ID.

    :param league_ids: Lista ID lig, które mają być pobrane.
    :return: Słownik z informacjami o ligach lub komunikat o błędzie.
    """
    client = APIClient()
    leagues_data = {}

    for league_id in league_ids:
        endpoint = f"/leagues?id={league_id}"
        response = client.get(endpoint)

        if response and "response" in response:
            leagues_data[league_id] = response["response"]
        else:
            leagues_data[league_id] = {"error": f"Brak danych dla ligi ID: {league_id}"}
    
    return leagues_data

if __name__ == "__main__":
    # Lista ID lig do pobrania
    league_ids = [
        144, 61, 71, 39, 78, 135, 88, 94, 179, 180, 62, 2, 301, 303, 203, 204, 206,
        233, 197, 79, 81, 188, 219, 218, 322, 119, 120, 380, 305, 40, 45, 48, 41,
        42, 43, 417, 17, 25, 141, 136, 89, 95, 207, 90, 145, 286, 307, 274, 323, 107, 345
    ]

    leagues = fetch_leagues(league_ids)

    for league_id, info in leagues.items():
        if "error" in info:
            print(f"Liga ID {league_id}: {info['error']}")
        else:
            print(f"Liga ID {league_id}: {info}")
