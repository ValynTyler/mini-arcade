class DPad:
    def __init__(self):
        self.up: bool = False
        self.down: bool = False
        self.left: bool = False
        self.right: bool = False


class Joystick:
    def __init__(self):
        self.x: float = 0
        self.y: float = 0


class Controller:
    def __init__(self):
        self.dpad: DPad = DPad()
        self.joystick = Joystick()

    def print(self):
        print(
            "dpad(" +
            "up",
            int(self.dpad.up),
            "down",
            int(self.dpad.down),
            "left",
            int(self.dpad.left),
            "right",
            str(int(self.dpad.right)) +
            ")",
        )
