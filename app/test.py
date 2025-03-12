import requests
import base64

# Encode Python code in base64
python_code = 'print("Im beginning to feel like a rap god.!")'
encoded_code = base64.b64encode(python_code.encode()).decode()

# Send request
response = requests.post("http://127.0.0.1:8000/execute", json={"language": "python", "code": encoded_code})

# Print response
print(response.json())
