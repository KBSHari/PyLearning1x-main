import requests

def get_request():
    response_body=requests.get(url="https://restful-booker.herokuapp.com/booking/1")
    print(response_body.status_code)
    print(response_body.json())
    data=response_body.json()
    assert response_body.status_code==200

    # Verification of value
    assert data["firstname"]=="Susan","Incorrect firstname"
    assert data["lastname"]=="Wilson","Incorrect lastname"
    assert data["bookingdates"]["checkout"]=="2022-09-15" ,"Incorrect checkout"

    #Verification of key

    assert "firstname" in data , "Incorrect firstname key"
    assert "lastname" in data , "Incorrect lastname key"



get_request()
