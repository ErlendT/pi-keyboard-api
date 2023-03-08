from app.hid_map import HID_MAP

NULL_CHAR = chr(0)
RELEASE_CHAR = NULL_CHAR*8

def send_string_as_keystrokes(data: str):
        for char in [*data]:
            if char.isupper():
                send_keystrokes(HID_MAP["KEY_MOD_RSHIFT"] + NULL_CHAR + HID_MAP[f"KEY_{char.upper()}"] +  NULL_CHAR*5)
            else:
                send_keystrokes(NULL_CHAR*2 + HID_MAP[f"KEY_{char.upper()}"] +  NULL_CHAR*5)
            # Release keys
            send_keystrokes(RELEASE_CHAR)


def send_keystrokes(input):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(input.encode())