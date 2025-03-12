import pytest
import base64
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_execute_endpoint():
    """Test if the /execute endpoint correctly processes Python code."""
    
    python_code = 'print("Hello from test!")'
    encoded_code = base64.b64encode(python_code.encode()).decode()

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/execute", json={"language": "python", "code": encoded_code})

    assert response.status_code == 200
    assert "execution_id" in response.json()
    assert "output" in response.json()
    assert "Hello from test!" in response.json()["output"]

@pytest.mark.asyncio
async def test_invalid_language():
    """Ensure that only Python is accepted."""
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/execute", json={"language": "javascript", "code": "console.log('Hello');"})

    assert response.status_code == 400
    assert response.json()["detail"] == "Only Python is supported."
