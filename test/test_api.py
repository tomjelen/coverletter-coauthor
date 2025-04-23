from unittest.mock import AsyncMock
import pytest
from fastapi.testclient import TestClient

from rest_api.api import app, get_llm
from rest_api.llm import LLM


@pytest.fixture
def mock_llm():
    mock = AsyncMock(spec=LLM)
    mock.generate_coverletter.return_value = "Default cover letter"
    return mock


@pytest.fixture
def client(mock_llm):
    """Fixture to create a test client for the FastAPI app."""
    app.dependency_overrides[get_llm] = lambda: mock_llm
    yield TestClient(app)
    app.dependency_overrides.clear()  # Avoid inter-dependencies between tests


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


def test_generate_prompts_llm(client, mock_llm):
    """Test the coverletters/generate endpoint uses the LLM."""
    mock_llm.generate_coverletter.return_value = "GENERATED COVER LETTER"

    response = client.post(
        "coverletters/generate",
        json={
            "job_description": "JOB DESCRIPTION",
            "applicant_name": "APPLICANT NAME",
        },
    )

    assert response.status_code == 200
    mock_llm.generate_coverletter.assert_called_once_with(
        "JOB DESCRIPTION", "APPLICANT NAME"
    )
    assert response.json()["cover_letter_markdown"] == "GENERATED COVER LETTER"
