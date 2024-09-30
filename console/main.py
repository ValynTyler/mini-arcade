import asyncio
import threading

from websockets.asyncio.server import serve, ServerConnection

from common.context import Context
from common.controller import Controller
from console.games import ping


class Server:
    controller = Controller()

    async def websocket_handler(self, websocket: ServerConnection):
        async for message in websocket:
            # print("Message received: " + message)
            self.controller.deserialize(message)
            await websocket.send(message)

    async def websocket_server(self):
        async with serve(self.websocket_handler, "localhost", 8765):
            print("Starting WS server...")
            while not stop_event.is_set():
                await asyncio.sleep(1)


    def run(self):
        asyncio.run(self.websocket_server())


if __name__ == "__main__":
    ctx = Context(caption="server")

    stop_event = threading.Event()

    sv = Server()
    thread = threading.Thread(target=sv.run,)
    thread.start()

    c = Controller()
    game = ping.Game(ctx, sv.controller, c)
    game.start()

    stop_event.set()
