
import requests

class BookerClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def create_booking(self, payload: dict) -> requests.Response:
        """Sends a POST request to create a new booking."""
        url = f"{self.BASE_URL}/booking"
        return requests.post(url, json=payload, headers=self.headers)

    def get_booking(self, booking_id: int) -> requests.Response:
        """Sends a GET request to retrieve a booking by ID."""
        url = f"{self.BASE_URL}/booking/{booking_id}"
        return requests.get(url, headers=self.headers)
