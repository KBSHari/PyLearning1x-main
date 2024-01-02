import pytest
import requests

@pytest.mark.postive
def test_post_request():
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
    data=response_body.json()
    print(data)

    # verification
    assert response_body.status_code==200
    assert data["booking"]["firstname"] is not None ,"Firstname not present"




