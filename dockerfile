FROM python:3.9-slim

WORKDIR /chromadb_mod

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "fastapi:app", "--host", "0.0.0.0", "--port", "8080"]
