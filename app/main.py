from typing import Union
from fastapi import FastAPI

from app.models.keyboard import KeyboardInputModel

app = FastAPI()

@app.post("/inputs")
def insert_input(keyboard_input: KeyboardInputModel):
    return keyboard_input

@app.get("/")
def read_root():
    return {"Hello": "World"}
