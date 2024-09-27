import pygame

from common.context import Context
from common.controller import Controller


class Emulator:
    def __init__(self):
        self.controller = Controller()

    def start(self):
        loop = ctx.run(self.update)
        loop()

    def update(self):
        keys = pygame.key.get_pressed()
        self.controller.dpad.up = keys[pygame.K_w]
        self.controller.dpad.down = keys[pygame.K_s]
        self.controller.dpad.left = keys[pygame.K_a]
        self.controller.dpad.right = keys[pygame.K_d]

        print(self.controller)


if __name__ == "__main__":
    print("Starting emulator...")
    ctx = Context(width=200, height=200, caption="emulator")

    emu = Emulator()
    emu.start()
