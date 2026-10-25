
from fastapi import FastAPI, Request
import httpx

app = FastAPI()

BACKENDS = [
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8081",
]

current_backend = 0


@app.get("/")
async def home(request: Request):
    global current_backend

    backend_url = BACKENDS[current_backend]

    current_backend = (current_backend + 1) % len(BACKENDS)

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{backend_url}{request.url.path}"
        )

    return response.json()


@app.get("/health")
def health():
    return {"status": "load balancer is running"}
