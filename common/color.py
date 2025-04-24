from typing import ClassVar


class Color:
    WHITE: ClassVar["Color"]
    BLACK: ClassVar["Color"]

    r: int
    g: int
    b: int

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    @property
    def rgb(self):
        return (self.r, self.g, self.b)


Color.BLACK = Color(0, 0, 0)
Color.WHITE = Color(255, 255, 255)
