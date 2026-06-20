FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir mlflow tensorflow

CMD ["mlflow", "server",
     "--host", "0.0.0.0",
     "--port", "8080",
     "--backend-store-uri", "sqlite:///mlflow.db",
     "--default-artifact-root", "./mlartifacts",
     "--allowed-hosts", "*",
     "--cors-allowed-origins", "*"]
