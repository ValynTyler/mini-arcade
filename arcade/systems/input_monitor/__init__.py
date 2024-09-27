import asyncio
import threading

from classes.controller import Controller
from systems.context import Context


async def async_task(c: Controller, stop: threading.Event):
    while not stop.is_set():
        await asyncio.sleep(.5)
        c.dpad.left = True
        await asyncio.sleep(.5)
        c.dpad.left = False


def start_task(c: Controller, stop: threading.Event):
    asyncio.run(async_task(c, stop_event))


def update(cont: Controller):
    cont.print()


if __name__ == "__main__":
    ctx = Context(caption="input monitor")
    controller = Controller()
    stop_event = threading.Event()

    async_thread = threading.Thread(target=start_task, args=(controller, stop_event,))
    async_thread.start()

    loop = ctx.run(update)
    loop(controller)
    stop_event.set()

    async_thread.join()
