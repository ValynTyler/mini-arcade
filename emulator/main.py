import pygame
from websockets.sync.client import connect

from common.context import Context
from common.controller import Controller


class Emulator:
    def __init__(self):
        self.websocket = None
        self.controller = Controller()

    def start(self):
        with connect("ws://localhost:8765") as websocket:
            print("Connection established")
            websocket.send("Sending message from emulator")
            websocket.recv()

            self.websocket = websocket
            loop = ctx.run(self.update)
            loop()

    def update(self):
        clf = self.controller.__str__()

        keys = pygame.key.get_pressed()
        self.controller.dpad.up = keys[pygame.K_w]
        self.controller.dpad.down = keys[pygame.K_s]
        self.controller.dpad.left = keys[pygame.K_a]
        self.controller.dpad.right = keys[pygame.K_d]

        if clf != self.controller.__str__():
            self.websocket.send(self.controller.__str__())
            self.websocket.recv()


if __name__ == "__main__":
    print("Starting emulator...")
    ctx = Context(width=200, height=200, caption="emulator")
    emu = Emulator()
    emu.start()
