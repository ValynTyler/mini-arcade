import asyncio
import pygame

from classes.controller import Controller
from systems import emulator, context
from systems import input_monitor
from systems.context import game_loop

if __name__ == "__main__":
    # initialize pygame
    width = 700
    height = 500
    pygame.init()
    screen_size = (width, height)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("controller emulator")

async def run_concurrently():
    controller = Controller()

    input_monitor_task = asyncio.to_thread(input_monitor.update, controller)
    emulator_task = asyncio.to_thread(emulator.update, controller)
    await asyncio.gather(emulator_task, input_monitor_task)

# asyncio.run(run_concurrently())


@game_loop
def run():
    controller = Controller()
    emulator.update(controller)
    input_monitor.update(controller)

run()

