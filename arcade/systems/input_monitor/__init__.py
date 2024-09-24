import pygame
from classes.controller import Controller
from systems import context
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


def update(cont: Controller):
    cont.print()

if __name__ == "__main__":
    controller = Controller()
    f = game_loop(update)
    f(controller)
