import pytest
import base64
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

#THIS TEST REQIORES kubernetes cluster to be running

def test_kubernetes_job_execution():
    """Test if a Python script executes inside Kubernetes via FastAPI."""

    python_code = 'print("Hello from Kubernetes!")'
    encoded_code = base64.b64encode(python_code.encode()).decode()

    response = client.post("/execute", json={"language": "python", "code": encoded_code})

    assert response.status_code == 200
    assert "execution_id" in response.json()
    assert "output" in response.json()
    assert "Hello from Kubernetes!" in response.json()["output"]
