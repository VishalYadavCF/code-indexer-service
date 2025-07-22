import requests


def test_repo():
    # Change this to a public repo for testing
    test_repo_url = "https://github.com/anthdm/gstream.git"

    response = requests.post(
        "http://localhost:8015/clone-repo", json={"repo_url": test_repo_url}
    )

    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")


if __name__ == "__main__":
    test_repo()
