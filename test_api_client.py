from api_client import APIClient

def test_api_client():
    """
    Testuje podstawowe połączenie z API-Football za pomocą APIClient.
    """
    client = APIClient()
    endpoint = "/leagues"
    response = client.get(endpoint)

    if response and "errors" in response and response["errors"]:
        print("Błąd: Otrzymano odpowiedź z błędami:", response["errors"])
    elif response and "response" in response:
        print("Sukces! Otrzymano dane:")
        print(response["response"])
    else:
        print("Błąd: Brak odpowiedzi lub nieprawidłowy format odpowiedzi.")

if __name__ == "__main__":
    test_api_client()
