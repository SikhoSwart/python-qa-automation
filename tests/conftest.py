
import pytest
from api_clients.booker_client import BookerClient

@pytest.fixture
def api_client():
    """Fixture that initializes and provides the BookerClient instance."""
    return BookerClient()
