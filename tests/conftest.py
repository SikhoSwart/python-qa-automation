
import pytest
from api_clients.booker_client import BookerClient


@pytest.fixture
def api_client():
    """Fixture that initialises and provides the BookerClient instance."""
    return BookerClient()

@pytest.fixture
def auth_token(api_client):
    """Fixture that generates and provides an auth token."""
    token = api_client.get_auth_token()
    return token
