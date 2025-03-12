from kubernetes import client, config
import os

# Load Kubernetes configuration (for local Minikube setup)
config.load_kube_config()

# Define the Kubernetes namespace (default for Minikube)
NAMESPACE = os.getenv("K8S_NAMESPACE", "default")

# Use a Python 3.9 Docker image for running code
PYTHON_IMAGE = "python:3.9"

def create_k8s_job(job_name, python_code):
    """Creates a Kubernetes Job to execute the given Python code securely."""
    
    # Define the job specification
    job = client.V1Job(
        metadata=client.V1ObjectMeta(name=job_name),
        spec=client.V1JobSpec(
            template=client.V1PodTemplateSpec(
                spec=client.V1PodSpec(
                    restart_policy="Never",
                    containers=[
                        client.V1Container(
                            name="python-runner",
                            image=PYTHON_IMAGE,
                            command=["python", "-c", python_code],  # Run user code inside container
                        )
                    ]
                )
            ),
            backoff_limit=1,  # No retries on failure
        ),
    )

    # Create the job in Kubernetes
    api = client.BatchV1Api()
    api.create_namespaced_job(namespace=NAMESPACE, body=job)

    return job_name

def get_k8s_job_output(job_name):
    """Fetches logs from the Kubernetes pod running the job."""
    
    api = client.CoreV1Api()
    
    # Get the pod name that matches the job
    pod_list = api.list_namespaced_pod(NAMESPACE, label_selector=f"job-name={job_name}")
    
    if not pod_list.items:
        return "No pod found for this job."

    pod_name = pod_list.items[0].metadata.name

    # Retrieve and return logs from the pod
    logs = api.read_namespaced_pod_log(name=pod_name, namespace=NAMESPACE)
    return logs
