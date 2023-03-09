from typing import Union
from fastapi import FastAPI, HTTPException

from app.models.keyboard import KeyboardInputModel
from app.keyboard_input import send_string_as_keystrokes

app = FastAPI()

@app.post("/inputs")
def insert_input(keyboard_input: KeyboardInputModel):
    try:
        send_string_as_keystrokes(keyboard_input.input)
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": str(e)})
    return keyboard_input

@app.get("/")
def read_root():
    return {"Hello": "World"}
