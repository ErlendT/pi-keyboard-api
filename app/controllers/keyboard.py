from starlite import Controller, get, post
from app.models.keyboard import KeyboardInput

from app.hid_map import HID_MAP

class KeyboardInputController(Controller):
    path = "/inputs"

    @post()
    async def insert_input(self, data: KeyboardInput) -> KeyboardInput:
        NULL_CHAR = chr(0)
        RELEASE_CHAR = NULL_CHAR*8

        for char in [*data.input]:
            if char.isupper():
                send_keystrokes(HID_MAP["KEY_MOD_RSHIFT"] + NULL_CHAR + HID_MAP[f"KEY_{char.upper()}"] +  NULL_CHAR*5)
            else:
                send_keystrokes(NULL_CHAR*2 + HID_MAP[f"KEY_{char.upper()}"] +  NULL_CHAR*5)
            # Release keys
            send_keystrokes(RELEASE_CHAR)
        return {}
    
    @get()
    async def get_input(self) -> KeyboardInput:
        return {"hello":"world"}

def send_keystrokes(input):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(input.encode())