from fetch_leagues import fetch_leagues

def test_fetch_leagues():
    """
    Testuje funkcję fetch_leagues z przykładowymi ID lig.
    """
    league_ids = [39, 78, 135, 88]  # Przykładowe ID lig
    leagues = fetch_leagues(league_ids)

    for league_id, info in leagues.items():
        if "error" in info:
            print(f"Błąd dla ligi ID {league_id}: {info['error']}")
        else:
            print(f"Sukces dla ligi ID {league_id}: {info}")

if __name__ == "__main__":
    test_fetch_leagues()
