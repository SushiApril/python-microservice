import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import store_execution_result, get_execution_result

client = TestClient(app)

@pytest.fixture
def sample_execution():
    """Provide sample execution data."""
    return {
        "execution_id": "test-id-123",
        "code": "cHJpbnQoIkhlbGxvLCBXb3JsZCIp",  # Base64 for 'print("Hello, World")'
        "output": "Hello, World\n",
    }

def test_store_execution(sample_execution):
    """Test storing execution results in MongoDB through FastAPI."""
    
    # Store execution result
    store_execution_result(**sample_execution)
    
    # Retrieve from MongoDB
    stored_result = get_execution_result("test-id-123")

    # Validate stored data
    assert stored_result is not None
    assert stored_result["execution_id"] == "test-id-123"
    assert stored_result["output"] == "Hello, World\n"

def test_get_execution_result(sample_execution):
    """Test retrieving execution results via FastAPI."""
    
    # First, store the result in MongoDB
    store_execution_result(**sample_execution)

    # Fetch using FastAPI endpoint
    response = client.get(f"/result/{sample_execution['execution_id']}")

    assert response.status_code == 200
    assert response.json()["execution_id"] == "test-id-123"
    assert response.json()["output"] == "Hello, World\n"
