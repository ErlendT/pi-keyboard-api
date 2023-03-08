
HID_MAP = {
    #
    # Modifier masks - used for the first byte in the HID report.
    # NOTE: The second byte in the report is reserved, \\x00
    #
    "KEY_MOD_LCTRL": "\\x01",
    "KEY_MOD_LSHIFT": "\\x02",
    "KEY_MOD_LALT": "\\x04",
    "KEY_MOD_LMETA": "\\x08",
    "KEY_MOD_RCTRL": "\\x10",
    "KEY_MOD_RSHIFT": "\\x20",
    "KEY_MOD_RALT": "\\x40",
    "KEY_MOD_RMETA": "\\x80",
    #
    # Scan codes - last N slots in the HID report (usually 6).
    # \\x00 if no key pressed.
    # 
    # If more than N keys are pressed, the HID reports 
    # KEY_ERR_OVF in all slots to indicate this condition.
    #
    "KEY_NONE": "\\x00", # No key pressed
    "KEY_ERR_OVF": "\\x01", #  Keyboard Error Roll Over - used for all slots if too many keys are pressed ("Phantom key")
    # \\x02 //  Keyboard POST Fail
    # \\x03 //  Keyboard Error Undefined
    "KEY_A": "\\x04", # Keyboard a and A
    "KEY_B": "\\x05", # Keyboard b and B
    "KEY_C": "\\x06", # Keyboard c and C
    "KEY_D": "\\x07", # Keyboard d and D
    "KEY_E": "\\x08", # Keyboard e and E
    "KEY_F": "\\x09", # Keyboard f and F
    "KEY_G": "\\x0a", # Keyboard g and G
    "KEY_H": "\\x0b", # Keyboard h and H
    "KEY_I": "\\x0c", # Keyboard i and I
    "KEY_J": "\\x0d", # Keyboard j and J
    "KEY_K": "\\x0e", # Keyboard k and K
    "KEY_L": "\\x0f", # Keyboard l and L
    "KEY_M": "\\x10", # Keyboard m and M
    "KEY_N": "\\x11", # Keyboard n and N
    "KEY_O": "\\x12", # Keyboard o and O
    "KEY_P": "\\x13", # Keyboard p and P
    "KEY_Q": "\\x14", # Keyboard q and Q
    "KEY_R": "\\x15", # Keyboard r and R
    "KEY_S": "\\x16", # Keyboard s and S
    "KEY_T": "\\x17", # Keyboard t and T
    "KEY_U": "\\x18", # Keyboard u and U
    "KEY_V": "\\x19", # Keyboard v and V
    "KEY_W": "\\x1a", # Keyboard w and W
    "KEY_X": "\\x1b", # Keyboard x and X
    "KEY_Y": "\\x1c", # Keyboard y and Y
    "KEY_Z": "\\x1d", # Keyboard z and Z

    "KEY_1": "\\x1e", # Keyboard 1 and !
    "KEY_2": "\\x1f", # Keyboard 2 and @
    "KEY_3": "\\x20", # Keyboard 3 and #
    "KEY_4": "\\x21", # Keyboard 4 and $
    "KEY_5": "\\x22", # Keyboard 5 and %
    "KEY_6": "\\x23", # Keyboard 6 and ^
    "KEY_7": "\\x24", # Keyboard 7 and &
    "KEY_8": "\\x25", # Keyboard 8 and *
    "KEY_9": "\\x26", # Keyboard 9 and (
    "KEY_0": "\\x27", # Keyboard 0 and )

    "KEY_ENTER": "\\x28", # Keyboard Return (ENTER)
    "KEY_ESC": "\\x29", # Keyboard ESCAPE
    "KEY_BACKSPACE": "\\x2a", # Keyboard DELETE (Backspace)
    "KEY_TAB": "\\x2b", # Keyboard Tab
    "KEY_SPACE": "\\x2c", # Keyboard Spacebar
    "KEY_MINUS": "\\x2d", # Keyboard - and _
    "KEY_EQUAL": "\\x2e", # Keyboard = and +
    "KEY_LEFTBRACE": "\\x2f", # Keyboard [ and {
    "KEY_RIGHTBRACE": "\\x30", # Keyboard ] and }
    "KEY_BACKSLASH": "\\x31", # Keyboard \ and |
    "KEY_HASHTILDE": "\\x32", # Keyboard Non-US # and ~
    "KEY_SEMICOLON": "\\x33", # Keyboard ; and :
    "KEY_APOSTROPHE": "\\x34", # Keyboard ' and "
    "KEY_GRAVE": "\\x35", # Keyboard ` and ~
    "KEY_COMMA": "\\x36", # Keyboard , and <
    "KEY_DOT": "\\x37", # Keyboard . and >
    "KEY_SLASH": "\\x38", # Keyboard / and ?
    "KEY_CAPSLOCK": "\\x39", # Keyboard Caps Lock

    "KEY_F1": "\\x3a", # Keyboard F1
    "KEY_F2": "\\x3b", # Keyboard F2
    "KEY_F3": "\\x3c", # Keyboard F3
    "KEY_F4": "\\x3d", # Keyboard F4
    "KEY_F5": "\\x3e", # Keyboard F5
    "KEY_F6": "\\x3f", # Keyboard F6
    "KEY_F7": "\\x40", # Keyboard F7
    "KEY_F8": "\\x41", # Keyboard F8
    "KEY_F9": "\\x42", # Keyboard F9
    "KEY_F10": "\\x43", # Keyboard F10
    "KEY_F11": "\\x44", # Keyboard F11
    "KEY_F12": "\\x45", # Keyboard F12

    "KEY_SYSRQ": "\\x46", # Keyboard Print Screen
    "KEY_SCROLLLOCK": "\\x47", # Keyboard Scroll Lock
    "KEY_PAUSE": "\\x48", # Keyboard Pause
    "KEY_INSERT": "\\x49", # Keyboard Insert
    "KEY_HOME": "\\x4a", # Keyboard Home
    "KEY_PAGEUP": "\\x4b", # Keyboard Page Up
    "KEY_DELETE": "\\x4c", # Keyboard Delete Forward
    "KEY_END": "\\x4d", # Keyboard End
    "KEY_PAGEDOWN": "\\x4e", # Keyboard Page Down
    "KEY_RIGHT": "\\x4f", # Keyboard Right Arrow
    "KEY_LEFT": "\\x50", # Keyboard Left Arrow
    "KEY_DOWN": "\\x51", # Keyboard Down Arrow
    "KEY_UP": "\\x52", # Keyboard Up Arrow

    "KEY_NUMLOCK": "\\x53", # Keyboard Num Lock and Clear
    "KEY_KPSLASH": "\\x54", # Keypad /
    "KEY_KPASTERISK": "\\x55", # Keypad *
    "KEY_KPMINUS": "\\x56", # Keypad -
    "KEY_KPPLUS": "\\x57", # Keypad +
    "KEY_KPENTER": "\\x58", # Keypad ENTER
    "KEY_KP1": "\\x59", # Keypad 1 and End
    "KEY_KP2": "\\x5a", # Keypad 2 and Down Arrow
    "KEY_KP3": "\\x5b", # Keypad 3 and PageDn
    "KEY_KP4": "\\x5c", # Keypad 4 and Left Arrow
    "KEY_KP5": "\\x5d", # Keypad 5
    "KEY_KP6": "\\x5e", # Keypad 6 and Right Arrow
    "KEY_KP7": "\\x5f", # Keypad 7 and Home
    "KEY_KP8": "\\x60", # Keypad 8 and Up Arrow
    "KEY_KP9": "\\x61", # Keypad 9 and Page Up
    "KEY_KP0": "\\x62", # Keypad 0 and Insert
    "KEY_KPDOT": "\\x63", # Keypad . and Delete

    "KEY_102ND": "\\x64", # Keyboard Non-US \ and |
    "KEY_COMPOSE": "\\x65", # Keyboard Application
    "KEY_POWER": "\\x66", # Keyboard Power
    "KEY_KPEQUAL": "\\x67", # Keypad =

    "KEY_F13": "\\x68", # Keyboard F13
    "KEY_F14": "\\x69", # Keyboard F14
    "KEY_F15": "\\x6a", # Keyboard F15
    "KEY_F16": "\\x6b", # Keyboard F16
    "KEY_F17": "\\x6c", # Keyboard F17
    "KEY_F18": "\\x6d", # Keyboard F18
    "KEY_F19": "\\x6e", # Keyboard F19
    "KEY_F20": "\\x6f", # Keyboard F20
    "KEY_F21": "\\x70", # Keyboard F21
    "KEY_F22": "\\x71", # Keyboard F22
    "KEY_F23": "\\x72", # Keyboard F23
    "KEY_F24": "\\x73", # Keyboard F24

    "KEY_OPEN": "\\x74", # Keyboard Execute
    "KEY_HELP": "\\x75", # Keyboard Help
    "KEY_PROPS": "\\x76", # Keyboard Menu
    "KEY_FRONT": "\\x77", # Keyboard Select
    "KEY_STOP": "\\x78", # Keyboard Stop
    "KEY_AGAIN": "\\x79", # Keyboard Again
    "KEY_UNDO": "\\x7a", # Keyboard Undo
    "KEY_CUT": "\\x7b", # Keyboard Cut
    "KEY_COPY": "\\x7c", # Keyboard Copy
    "KEY_PASTE": "\\x7d", # Keyboard Paste
    "KEY_FIND": "\\x7e", # Keyboard Find
    "KEY_MUTE": "\\x7f", # Keyboard Mute
    "KEY_VOLUMEUP": "\\x80", # Keyboard Volume Up
    "KEY_VOLUMEDOWN": "\\x81", # Keyboard Volume Down
    # \\x82  Keyboard Locking Caps Lock
    # \\x83  Keyboard Locking Num Lock
    # \\x84  Keyboard Locking Scroll Lock
    "KEY_KPCOMMA": "\\x85", # Keypad Comma
    # \\x86  Keypad Equal Sign
    "KEY_RO": "\\x87", # Keyboard International1
    "KEY_KATAKANAHIRAGANA": "\\x88", # Keyboard International2
    "KEY_YEN": "\\x89", # Keyboard International3
    "KEY_HENKAN": "\\x8a", # Keyboard International4
    "KEY_MUHENKAN": "\\x8b", # Keyboard International5
    "KEY_KPJPCOMMA": "\\x8c", # Keyboard International6
    # \\x8d  Keyboard International7
    # \\x8e  Keyboard International8
    # \\x8f  Keyboard International9
    "KEY_HANGEUL": "\\x90", # Keyboard LANG1
    "KEY_HANJA": "\\x91", # Keyboard LANG2
    "KEY_KATAKANA": "\\x92", # Keyboard LANG3
    "KEY_HIRAGANA": "\\x93", # Keyboard LANG4
    "KEY_ZENKAKUHANKAKU": "\\x94", # Keyboard LANG5
    # \\x95  Keyboard LANG6
    # \\x96  Keyboard LANG7
    # \\x97  Keyboard LANG8
    # \\x98  Keyboard LANG9
    # \\x99  Keyboard Alternate Erase
    # \\x9a  Keyboard SysReq/Attention
    # \\x9b  Keyboard Cancel
    # \\x9c  Keyboard Clear
    # \\x9d  Keyboard Prior
    # \\x9e  Keyboard Return
    # \\x9f  Keyboard Separator
    # \\xa0  Keyboard Out
    # \\xa1  Keyboard Oper
    # \\xa2  Keyboard Clear/Again
    # \\xa3  Keyboard CrSel/Props
    # \\xa4  Keyboard ExSel

    # \\xb0  Keypad 00
    # \\xb1  Keypad 000
    # \\xb2  Thousands Separator
    # \\xb3  Decimal Separator
    # \\xb4  Currency Unit
    # \\xb5  Currency Sub-unit
    "KEY_KPLEFTPAREN": "\\xb6", # Keypad (
    "KEY_KPRIGHTPAREN": "\\xb7", # Keypad )
    # \\xb8  Keypad {
    # \\xb9  Keypad }
    # \\xba  Keypad Tab
    # \\xbb  Keypad Backspace
    # \\xbc  Keypad A
    # \\xbd  Keypad B
    # \\xbe  Keypad C
    # \\xbf  Keypad D
    # \\xc0  Keypad E
    # \\xc1  Keypad F
    # \\xc2  Keypad XOR
    # \\xc3  Keypad ^
    # \\xc4  Keypad %
    # \\xc5  Keypad <
    # \\xc6  Keypad >
    # \\xc7  Keypad &
    # \\xc8  Keypad &&
    # \\xc9  Keypad |
    # \\xca  Keypad ||
    # \\xcb  Keypad :
    # \\xcc  Keypad #
    # \\xcd  Keypad Space
    # \\xce  Keypad @
    # \\xcf  Keypad !
    # \\xd0  Keypad Memory Store
    # \\xd1  Keypad Memory Recall
    # \\xd2  Keypad Memory Clear
    # \\xd3  Keypad Memory Add
    # \\xd4  Keypad Memory Subtract
    # \\xd5  Keypad Memory Multiply
    # \\xd6  Keypad Memory Divide
    # \\xd7  Keypad +/-
    # \\xd8  Keypad Clear
    # \\xd9  Keypad Clear Entry
    # \\xda  Keypad Binary
    # \\xdb  Keypad Octal
    # \\xdc  Keypad Decimal
    # \\xdd  Keypad Hexadecimal

    "KEY_LEFTCTRL": "\\xe0", # Keyboard Left Control
    "KEY_LEFTSHIFT": "\\xe1", # Keyboard Left Shift
    "KEY_LEFTALT": "\\xe2", # Keyboard Left Alt
    "KEY_LEFTMETA": "\\xe3", # Keyboard Left GUI
    "KEY_RIGHTCTRL": "\\xe4", # Keyboard Right Control
    "KEY_RIGHTSHIFT": "\\xe5", # Keyboard Right Shift
    "KEY_RIGHTALT": "\\xe6", # Keyboard Right Alt
    "KEY_RIGHTMETA": "\\xe7", # Keyboard Right GUI

    #define KEY_MEDIA_PLAYPAUSE \\xe8
    #define KEY_MEDIA_STOPCD \\xe9
    #define KEY_MEDIA_PREVIOUSSONG \\xea
    #define KEY_MEDIA_NEXTSONG \\xeb
    #define KEY_MEDIA_EJECTCD \\xec
    #define KEY_MEDIA_VOLUMEUP \\xed
    #define KEY_MEDIA_VOLUMEDOWN \\xee
    #define KEY_MEDIA_MUTE \\xef
    #define KEY_MEDIA_WWW \\xf0
    #define KEY_MEDIA_BACK \\xf1
    #define KEY_MEDIA_FORWARD \\xf2
    #define KEY_MEDIA_STOP \\xf3
    #define KEY_MEDIA_FIND \\xf4
    #define KEY_MEDIA_SCROLLUP \\xf5
    #define KEY_MEDIA_SCROLLDOWN \\xf6
    #define KEY_MEDIA_EDIT \\xf7
    #define KEY_MEDIA_SLEEP \\xf8
    #define KEY_MEDIA_COFFEE \\xf9
    #define KEY_MEDIA_REFRESH \\xfa
    #define KEY_MEDIA_CALC \\xfb

}
