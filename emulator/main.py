from uu import Error

import pygame
from websockets.sync.client import connect

from common.context import Context
from common.controller import Controller


class Emulator:
    def __init__(self):
        self.websocket = None
        self.controller_1 = Controller()
        self.controller_2 = Controller()

    def start(self):
        with connect("ws://localhost:8765") as websocket:
            print("Connection established")
            # websocket.send("Sending message from emulator")
            # websocket.recv()

            self.websocket = websocket
            loop = ctx.run(self.update)
            loop()

    def update(self):
        c1_lf = self.controller_1.serialize()
        c2_lf = self.controller_2.serialize()
        keys = pygame.key.get_pressed()

        self.controller_1.dpad.up = keys[pygame.K_w]
        self.controller_1.dpad.down = keys[pygame.K_s]
        self.controller_1.dpad.left = keys[pygame.K_a]
        self.controller_1.dpad.right = keys[pygame.K_d]

        self.controller_2.dpad.up = keys[pygame.K_UP]
        self.controller_2.dpad.down = keys[pygame.K_DOWN]
        self.controller_2.dpad.left = keys[pygame.K_LEFT]
        self.controller_2.dpad.right = keys[pygame.K_RIGHT]

        if c1_lf != self.controller_1.serialize():
            self.websocket.send(self.controller_1.serialize())
            self.websocket.recv()


if __name__ == "__main__":
    print("Starting emulator...")
    ctx = Context(width=200, height=200, caption="emulator")
    emu = Emulator()
    emu.start()
