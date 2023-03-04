from starlite import Starlite

from app.controllers.keyboard import KeyboardInputController

app = Starlite(route_handlers=[KeyboardInputController])