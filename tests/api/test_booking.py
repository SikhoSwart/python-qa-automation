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

def test_create_booking_successfully(api_client):
    #prepare test data
    payload = {
        "firstname": "Alex",
        "lastname": "Tester",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-05"
        },
        "additionalneeds": "Late Checkout"
    }

    #Send request via client
    response = api_client.create_booking(payload)

    #Verify response details
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"

    data = response.json()

    # Verify top-level structure
    assert "bookingid" in data
    assert isinstance(data["bookingid"], int)

    # Verify returned payload matches input
    booking = data["booking"]
    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]
    assert booking["totalprice"] == payload["totalprice"]
    assert booking["depositpaid"] is True
    assert booking["bookingdates"]["checkin"] == payload["bookingdates"]["checkin"]

    # Simple performance check (response under 2 seconds)
    assert response.elapsed.total_seconds() < 2.0

def test_update_booking_successfully(api_client, auth_token):
    #Create a booking first
    initial_payload = {
        "firstname": "John", "lastname": "Doe", "totalprice": 100,
        "depositpaid": True, "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"}
    }
    create_resp = api_client.create_booking(initial_payload)
    booking_id = create_resp.json()["bookingid"]

    #Update the booking (change price to 999)
    updated_payload = initial_payload.copy()
    updated_payload["totalprice"] = 999

    update_resp = api_client.update_booking(booking_id, updated_payload, auth_token)

    #Assert
    assert update_resp.status_code == 200
    assert update_resp.json()["totalprice"] == 999

def test_delete_booking_successfully(api_client, auth_token):
    # Create a booking to delete
    payload = {
        "firstname": "Delete", "lastname": "Me", "totalprice": 50,
        "depositpaid": False, "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-02"}
    }
    create_resp = api_client.create_booking(payload)
    booking_id = create_resp.json()["bookingid"]

    #Delete the booking
    delete_resp = api_client.delete_booking(booking_id, auth_token)

    # Restful-Booker returns 201 Created for a successful delete
    assert delete_resp.status_code == 201

    #Verify it's actually gone by trying to GET it
    get_resp = api_client.get_booking(booking_id)
    assert get_resp.status_code == 404 # Not Found
