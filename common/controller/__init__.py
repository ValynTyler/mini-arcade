from common.controller.dpad import DPad
from common.controller.joystick import Joystick


class Controller:
    def __init__(self):
        self.dpad: DPad = DPad()
        self.joystick: Joystick = Joystick()

    def __str__(self):
        return (
            f"dpad("
            f"{int(self.dpad.up)}"
            f"{int(self.dpad.down)}"
            f"{int(self.dpad.left)}"
            f"{int(self.dpad.right)}"
            f")"
        )

    def serialize(self) -> str:
        return (
            f"{int(self.dpad.up)}"
            f"{int(self.dpad.down)}"
            f"{int(self.dpad.left)}"
            f"{int(self.dpad.right)}"
        )

    def deserialize(self, data: str):
        self.dpad.up = bool(int(data[0]))
        self.dpad.down = bool(int(data[1]))
        self.dpad.left = bool(int(data[2]))
        self.dpad.right = bool(int(data[3]))
