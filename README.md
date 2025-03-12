# python-microservice
# Python Execution Microservice

## 📌 Overview

This project is a **FastAPI-based microservice** that allows users to execute Python code inside a **Kubernetes Job** and store the results in **MongoDB**.

## 🚀 Features

- **Run Python code securely inside Kubernetes**
- **Store execution results in MongoDB**
- **Retrieve past execution results**
- **Tested with FastAPI, pytest, and Kubernetes**

---

## 📂 Project Structure

```
python-microservice/
│── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI application
│   ├── database.py    # MongoDB integration
│   ├── k8s.py         # Kubernetes Job management
│   ├── job.yaml       # Kubernetes Job template
│── tests/
│   ├── test_main.py   # API tests
│   ├── test_database.py   # MongoDB tests
│   ├── test_k8s.py    # Kubernetes execution tests
│── requirements.txt   # Python dependencies
│── Dockerfile         # Docker containerization
│── pytest.ini         # Pytest configuration
│── README.md          # Documentation (this file)
```

---

## 🛠️ Setup & Installation

### **1️⃣ Install Dependencies**

Make sure you have **Python 3.11** installed. Then, install the required dependencies:

```sh
pip install -r requirements.txt
```

### **2️⃣ Start MongoDB (Docker Recommended)**

If you don’t have MongoDB installed, run it using Docker:

```sh
docker run -d --name mongo -p 27017:27017 mongo
```

### **3️⃣ Start FastAPI Server**

Run the API locally using Uvicorn:

```sh
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ FastAPI will now be running at `http://127.0.0.1:8000`.

---

## 📌 Usage

### **🔹 Run Python Code via API**

Send a `POST` request to `/execute` with a **base64-encoded** Python script.

#### **Example Request:**

```json
{
  "language": "python",
  "code": "cHJpbnQoIkhlbGxvLCBXb3JsZCIp"
}
```

(👆 `cHJpbnQoIkhlbGxvLCBXb3JsZCIp` is base64 for `print("Hello, World")`)

#### **Example Response:**

```json
{
  "execution_id": "123e4567-e89b-12d3-a456-426614174000",
  "output": "Hello, World\n"
}
```

### **🔹 Retrieve Execution Results**

Send a `GET` request to `/result/{execution_id}` to fetch previous execution results.

#### **Example Request:**

```sh
GET /result/123e4567-e89b-12d3-a456-426614174000
```

#### **Example Response:**

```json
{
  "execution_id": "123e4567-e89b-12d3-a456-426614174000",
  "code": "cHJpbnQoIkhlbGxvLCBXb3JsZCIp",
  "output": "Hello, World\n",
  "timestamp": "2025-03-12T12:00:00Z"
}
```

---

## ⚙️ Deploying to Kubernetes

1️⃣ **Ensure Minikube is running:**

```sh
minikube start
```

2️⃣ **Apply Kubernetes Job template:**

```sh
kubectl apply -f app/job.yaml
```

3️⃣ **Check Kubernetes Jobs and Pods:**

```sh
kubectl get jobs
kubectl get pods
```

4️⃣ **View logs from a running job:**

```sh
kubectl logs <pod-name>
```

---

## ✅ Running Tests

This project includes **unit tests** for API, MongoDB, and Kubernetes execution.

### **1️⃣ Run All Tests**

```sh
python3.11 -m pytest tests/
```

### **2️⃣ Run Specific Test Files**

```sh
python3.11 -m pytest tests/test_main.py   # API tests
python3.11 -m pytest tests/test_database.py   # MongoDB tests
python3.11 -m pytest tests/test_k8s.py   # Kubernetes execution tests
```

### **3️⃣ Run Tests with Verbose Output**

```sh
python3.11 -m pytest -v tests/
```



## 📝 License

This project is licensed under the MIT License (if needed, update accordingly).

---

## 📩 Contact

For any questions or suggestions, feel free to reach out to me at sushang1@uci.edu

