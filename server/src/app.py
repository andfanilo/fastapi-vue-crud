from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Pong(BaseModel):
    status: str
    code: int
    messages: List[str]
    result: str


@app.get("/ping", response_model=Pong)
def ping_pong():
    return {"status": "ok", "code": 200, "messages": [], "result": "Pong!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
