from app.hid_map import HID_MAP

NULL_CHAR = chr(0)
RELEASE_CHARS = NULL_CHAR*8

def send_string_as_keystrokes(data: str):
    # Release keys
    send_keystrokes(RELEASE_CHARS)
    for char in [*data]:
        send_keystrokes(HID_MAP[f"{char}"] + NULL_CHAR*5)
        # Release keys
        send_keystrokes(RELEASE_CHARS)


def send_keystrokes(input):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(input.encode())
