from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Pong(BaseModel):
    status: str
    code: int
    messages: List[str]
    result: str


@app.get("/ping", response_model=Pong)
def ping_pong():
    return {"status": "ok", "code": 200, "messages": [], "result": "pong!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0")
