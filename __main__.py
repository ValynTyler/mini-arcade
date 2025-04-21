#!/usr/bin/env python

import asyncio
import struct
from websockets.asyncio.server import serve


async def echo(websocket):
  async for message in websocket:
    value = struct.unpack('<I', message)[0]
    print('Controller state:', bin(value))
    await websocket.send(message)


async def main():
  try:
    port = 8000
    print(f'Opening WS server at ws://localhost:{port}.')
    async with serve(echo, '0.0.0.0', port):
      await asyncio.get_running_loop().create_future()
  except:
    print('\nClosing WS server...')


asyncio.run(main())
