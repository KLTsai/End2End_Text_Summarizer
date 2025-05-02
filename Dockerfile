FROM python:3.10-slim-buster


WORKDIR /app


RUN apt-get update -y && apt-get install -y \
    awscli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
COPY . .


RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir --upgrade transformers accelerate \
    && pip install --no-cache-dir uvicorn


EXPOSE 8080


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]