import asyncio
import threading

import pygame
import websockets
from websockets.asyncio.client import connect

from common.context import Context
from common.controller import Controller


async def websocket_client(uri):
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        await websocket.send("Hello, Server!")
        print(f"> Sent: Hello, Server!")

        # Wait for a response from the server
        response = await websocket.recv()
        print(f"< Received: {response}")


class Emulator:
    websocket_url = "localhost:8765"
    websocket = None

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

    async def connect_websocket(self):
        with connect(self.websocket_url) as websocket:
            self.websocket = websocket
            print("Websocket connected successfully")

    def websocket_client(self):
        asyncio.run(self.connect_websocket())


if __name__ == "__main__":
    print("Starting emulator...")
    ctx = Context(width=200, height=200, caption="emulator")
    emu = Emulator()

    ws_thread = threading.Thread(target=emu.websocket_client())

    emu.start()
