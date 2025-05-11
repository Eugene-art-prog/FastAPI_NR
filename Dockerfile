
FROM python:3.13.3
WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .
RUN pip install -r requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
