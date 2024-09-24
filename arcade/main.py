import asyncio
import pygame

from classes.controller import Controller
from systems import emulator
from systems import input_monitor

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
    emulator_task = asyncio.to_thread(emulator.run, controller)
    monitor_task = asyncio.to_thread(input_monitor.run, controller)

    await asyncio.gather(emulator_task, monitor_task)

asyncio.run(run_concurrently())
