FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install mlflow tensorflow

CMD mlflow server \
    --host 0.0.0.0 \
    --port $PORT \
    --backend-store-uri sqlite:///mlflow.db \
    --default-artifact-root ./mlartifacts
