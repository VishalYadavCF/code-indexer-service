import requests

def test_healthcheck():
    response = requests.get("http://localhost:8015/healthcheck")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    print("Healthcheck passed!")

if __name__ == "__main__":
    test_healthcheck()

