
import pytest
from api_clients.booker_client import BookerClient

def test_create_booking():
    client = BookerClient()
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-05"}
    }
    response = client.create_booking(payload)
    
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == "Jim"
