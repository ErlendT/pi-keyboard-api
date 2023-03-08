from typing import Union
from fastapi import FastAPI

from app.models.keyboard import KeyboardInputModel
from app.keyboard_input import send_string_as_keystrokes

app = FastAPI()

@app.post("/inputs", status_code=202)
def insert_input(keyboard_input: KeyboardInputModel):
    send_string_as_keystrokes(keyboard_input.input)
    return keyboard_input

@app.get("/")
def read_root():
    return {"Hello": "World"}
