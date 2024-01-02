import pytest
import requests


def test_get_request():
    response_body = requests.get(url="https://restful-booker.herokuapp.com/booking/1")

    print(response_body.json())
    data = response_body.json()


    assert response_body.status_code == 200

    # Verification of value
    assert data["firstname"] == "Eric", "Incorrect firstname"
    assert data["lastname"] == "Brown", "Incorrect lastname"

    # Verification of key

    assert "firstname" in data, "Incorrect firstname key"
    assert "lastname" in data, "Incorrect lastname key"