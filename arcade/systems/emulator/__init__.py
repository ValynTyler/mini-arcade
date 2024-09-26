import asyncio

import pygame

from classes.controller import Controller
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


def update(controller: Controller, use_arrow_keys: bool = False):
    keys = pygame.key.get_pressed()
    if use_arrow_keys:
        controller.dpad.up = keys[pygame.K_UP]
        controller.dpad.down = keys[pygame.K_DOWN]
        controller.dpad.left = keys[pygame.K_LEFT]
        controller.dpad.right = keys[pygame.K_RIGHT]
    else:
        controller.dpad.up = keys[pygame.K_w]
        controller.dpad.down = keys[pygame.K_s]
        controller.dpad.left = keys[pygame.K_a]
        controller.dpad.right = keys[pygame.K_d]


if __name__ == "__main__":
    controller = Controller()


    async def async_emulator():
        emulator_task = asyncio.to_thread(update, controller, False)
        monitor_task = asyncio.to_thread(input_monitor.update, controller)
        await asyncio.gather(emulator_task, monitor_task)


    asyncio.run(async_emulator())
