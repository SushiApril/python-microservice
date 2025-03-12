import pytest
import base64
from fastapi.testclient import TestClient
from app.main import app

# Create a test client for FastAPI
client = TestClient(app)

def test_execute_endpoint():
    """Test if the /execute endpoint correctly processes Python code."""
    
    python_code = 'print("Hello from test!")'
    encoded_code = base64.b64encode(python_code.encode()).decode()

    response = client.post("/execute", json={"language": "python", "code": encoded_code})

    assert response.status_code == 200
    assert "execution_id" in response.json()
    assert "output" in response.json()
    assert "Hello from test!" in response.json()["output"]

def test_invalid_language():
    """Ensure that only Python is accepted."""
    
    response = client.post("/execute", json={"language": "javascript", "code": "console.log('Hello');"})

    assert response.status_code == 400
    assert response.json()["detail"] == "Only Python is supported."
