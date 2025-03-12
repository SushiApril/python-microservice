import requests
import base64

# Encode Python code in base64
python_code = 'print("east is up im fearless when i hear this on the low, east is up im fearless when i wear my rebel clothes east is up.!")'
encoded_code = base64.b64encode(python_code.encode()).decode()

# Send request
#response = requests.post("http://127.0.0.1:8000/execute", json={"language": "python", "code": encoded_code})

# Print response
#print(response.json())


execution_id = "c1329357-11e4-4f56-9bde-e3c50186caf7"  # Replace with your execution ID
response = requests.get(f"http://127.0.0.1:8000/result/{execution_id}")

print(response.json())