import requests
import os

def test_list_files():
    repo_relative_path = "../cloned_repos/gstream"
    repo_abs_path = os.path.abspath(repo_relative_path)
    url = "http://localhost:8015/list-files"
    payload = {"repo_path": repo_abs_path}
    response = requests.post(url, json=payload)
    print("Status code:", response.status_code)
    print("Response:", response.json())
    assert response.status_code == 200
    assert "files" in response.json()
    assert any(f.endswith("main.go") for f in response.json()["files"])
    print("Test passed: main.go found in file list.")

if __name__ == "__main__":
    test_list_files()
