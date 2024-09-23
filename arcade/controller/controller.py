from controller.dpad import DPad
from controller.joystick import Joystick

class Controller:
    def __init__(self):
        self.dpad: DPad = DPad()
        self.joystick = Joystick()

    def print(self):
        print(f"dpad("
              f"{int(self.dpad.up)}"
              f"{int(self.dpad.down)}"
              f"{int(self.dpad.left)}"
              f"{int(self.dpad.right)}"
              f")"
              )
