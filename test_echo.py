import requests

BASE_URL = "https://postman-echo.com"

def test1_get_with_query_params():
    params = {"name": "Олюша", "age": 19}
    response = requests.get(f"{BASE_URL}/get", params=params)
    assert response.status_code == 200
    data = response.json()
    assert data["args"]["name"] == "Олюша"
    assert data["args"]["age"] == "19"

def test2_get_headers():
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200
    data = response.json()
    assert "headers" in data
    assert "host" in data["headers"]

def test3_post_json():
    json_data = {"message": "Hello, Netology"}
    response = requests.post(f"{BASE_URL}/post", json=json_data)
    assert response.status_code == 200
    data = response.json()
    assert data["json"] == json_data

def test4_post_form():
    form = {"username": "Olyusha", "password": "hidden321"}
    response = requests.post(f"{BASE_URL}/post", data=form)
    assert response.status_code == 200
    data = response.json()
    assert data["form"]["username"] == "Olyusha"
    assert data["form"]["password"] == "hidden321"

def test5_post_with_query_and_body():
    params = {"token": "a1b2c3", "version": "1.0"}
    json_body = {"action": "login", "device": "mobile"}
    response = requests.post(f"{BASE_URL}/post", params=params, json=json_body)
    assert response.status_code == 200
    data = response.json()
    assert data["args"]["token"] == "a1b2c3"
    assert data["args"]["version"] == "1.0"
    assert data["json"]["action"] == "login"
    assert data["json"]["device"] == "mobile"

if __name__ == "__main__":
    test1_get_with_query_params()
    test2_get_headers()
    test3_post_json()
    test4_post_form()
    test5_post_with_query_and_body()
