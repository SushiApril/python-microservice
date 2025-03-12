from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import base64
import uuid
from app.k8s import create_k8s_job, get_k8s_job_output
import time

app = FastAPI()

# Request model for execution
class ExecutionRequest(BaseModel):
    language: str
    code: str  # Base64-encoded Python code

# Response model for execution
class ExecutionResponse(BaseModel):
    execution_id: str
    output: str

@app.get("/")
def read_root():
    return {"message": "Python Execution Microservice is running!"}

@app.post("/execute", response_model=ExecutionResponse)
async def execute_code(request: ExecutionRequest):
    # Only allow Python for now
    if request.language.lower() != "python":
        raise HTTPException(status_code=400, detail="Only Python is supported.")

    try:
        # Decode the base64-encoded Python code
        decoded_code = base64.b64decode(request.code).decode("utf-8")

        # Generate a unique execution ID
        execution_id = str(uuid.uuid4())

        # Mock execution output (for now)
        job_name = f"exec-job-{execution_id[:8]}"
        create_k8s_job(job_name, decoded_code)
        time.sleep(3)
        output = get_k8s_job_output(job_name)

        return {"execution_id": execution_id, "output": output}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
