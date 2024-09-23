import pygame

from classes.controller import Controller

if __name__ == "__main__":
    # initialize pygame
    width = 700
    height = 500
    pygame.init()
    screen_size = (width, height)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("controller emulator")


def run(controller: Controller):
    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()

        controller.dpad.up = keys[pygame.K_w]
        controller.dpad.down = keys[pygame.K_s]
        controller.dpad.left = keys[pygame.K_a]
        controller.dpad.right = keys[pygame.K_d]


if __name__ == "__main__":
    run(Controller())
