import pytest
import requests


def create_token_request():
    URL = "https://restful-booker.herokuapp.com/auth"
    Payload = {
        "username": "admin",
        "password": "password123"
    }
    response_token = requests.post(url=URL, json=Payload)
    data = response_token.json()
    return data["token"]


def create_bookingId():
    URL = "https://restful-booker.herokuapp.com/booking"
    HEADER = {"Content-Type": "application/json"}
    JSON = {
        "firstname": "Jims",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_body = requests.post(url=URL, headers=HEADER, json=JSON)
    data = response_body.json()
    print(data["bookingid"])
    return data["bookingid"]


def test_put_request():
    id = str(create_bookingId())
    URL = "https://restful-booker.herokuapp.com/booking/" + id
    HEADER = {"Content-Type": "application/json", "Accept": "application/json",
              "Cookie": "token=" + create_token_request()}
    payload = {
        "firstname": "KBS",
        "lastname": "Hari",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_body = requests.put(url=URL, headers=HEADER, json=payload)
    print(response_body.json())


def test_delete_request():
    id = str(create_bookingId())
    URL = "https://restful-booker.herokuapp.com/booking/" + id
    HEADER = {"Content-Type": "application/json", "Accept": "application/json",
              "Cookie": "token=" + create_token_request()}
    response_body = requests.delete(url=URL, headers=HEADER)
    assert response_body.status_code == 201
