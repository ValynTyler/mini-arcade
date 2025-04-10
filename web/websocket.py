#!/usr/bin/env python

import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
  async for message in websocket:
    print('Message received: ' + message)
    await websocket.send(message)


async def main():
  try:
    port = 8765
    print(f'Opening WS server at ws://localhost:{port}.')
    async with serve(echo, 'localhost', 8765):
      await asyncio.get_running_loop().create_future()
  except:
    print('\nClosing WS server...')


asyncio.run(main())