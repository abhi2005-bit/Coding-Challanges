
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from Backend Server 2"}


@app.get("/health")
def health():
    return {"status": "healthy"}
