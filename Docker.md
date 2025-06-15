# 🐳 Docker Sandbox Setup

This app uses Docker to securely run AI-generated Python code in an isolated environment. Follow these steps to build the Docker image used during code execution.

---

## 📦 1. Create the Dockerfile

Create a file named `Dockerfile.sandbox` inside python-sandbox folder in your project root with the following contents:

```dockerfile
# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install common Python packages for data science and visualization
RUN pip install --no-cache-dir pandas matplotlib seaborn plotly pillow
```

---

## 🛠️ 2. Build the Docker Image

Run this command in Docker Desktop from the directory where `Dockerfile.sandbox` is located:
```bash
cd /AI-Data-Viz-App

docker build -f Dockerfile.sandbox -t python-sandbox .
```

This creates a Docker image named `python-sandbox`, which your app will use to execute generated Python code safely and reproducibly.

---

## ✅ 3. Verify the Image

Ensure the image is built by listing available Docker images:

```bash
docker images
```

You should see an entry for `python-sandbox`.

---

Now your sandbox is ready to run Python code securely inside Docker!
