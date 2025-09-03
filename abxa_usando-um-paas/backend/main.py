from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class UserRequest(BaseModel):
    user_name: str

@app.get("/")
def read_root():
    return {"abxa": "Atividade - Subindo EC2"}

@app.post("/auth/me")
def auth_me(request: UserRequest):
    username = request.user_name
    return {"user": username, "ping": "pong"}