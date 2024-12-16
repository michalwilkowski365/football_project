import requests

BASE_URL = "http://127.0.0.1:5000/api/matches"

def test_matches_endpoint():
    test_cases = [
        {"params": {"league": 188, "season": 2024, "date": "2024-12-15"}, "expected_status": 200},
        {"params": {"league": 188, "season": 2024}, "expected_status": 400},
        {"params": {"league": 188, "date": "2024-12-15"}, "expected_status": 400},
        {"params": {"season": 2024, "date": "2024-12-15"}, "expected_status": 400},
        {"params": {}, "expected_status": 400}
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"### Test {i}: {case['params']} ###")
        response = requests.get(BASE_URL, params=case["params"])
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        assert response.status_code == case["expected_status"], "Test failed!"

if __name__ == "__main__":
    test_matches_endpoint()
