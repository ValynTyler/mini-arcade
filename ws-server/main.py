import asyncio
from websockets.asyncio.server import serve

async def handler(websocket):
    async for message in websocket:
        print("Message received: " + message)

async def main():
    async with serve(handler, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

print("Starting WS server...")
asyncio.run(main())
