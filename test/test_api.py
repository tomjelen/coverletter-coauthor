import pytest
from fastapi.testclient import TestClient

from rest_api.api import app


@pytest.fixture
def client():
    """Fixture to create a test client for the FastAPI app."""
    return TestClient(app)


def test_generate_contract(client):
    """Test the coverletters/generate endpoint returns 200 OK."""
    response = client.post(
        "coverletters/generate",
        json={
            "job_description": "JD",
            "applicant_name": "John Doe",
        },
    )

    assert response.status_code == 200
    assert "cover_letter_markdown" in response.json().keys()
