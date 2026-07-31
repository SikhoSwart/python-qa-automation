
import pytest
import api_clients
from api_clients import booker_client


@pytest.fixture
def api_client():
    """Fixture that initializes and provides the BookerClient instance."""
    return booker_client.BookerClient()
