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

    def get_auth_token(self, username="admin", password="password123") -> str:
        """Authenticates and returns a session token."""
        url = f"{self.BASE_URL}/auth"
        payload = {"username": username, "password": password}
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()["token"]

    def update_booking(self, booking_id: int, payload: dict, token: str) -> requests.Response:
        """Sends a PUT request to update an entire booking."""
        url = f"{self.BASE_URL}/booking/{booking_id}"
        headers = self.headers.copy()
        headers["Cookie"] = f"token={token}"
        return requests.put(url, json=payload, headers=headers)

    def delete_booking(self, booking_id: int, token: str) -> requests.Response:
        """Sends a DELETE request to remove a booking."""
        url = f"{self.BASE_URL}/booking/{booking_id}"
        headers = self.headers.copy()
        headers["Cookie"] = f"token={token}"
        return requests.delete(url, headers=headers)
