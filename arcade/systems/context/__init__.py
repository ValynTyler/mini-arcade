import pygame


def game_loop(func):
    def inner(*args, **kwargs):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            # run lambda
            func(*args, **kwargs)
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

    return inner


class Context:
    def __init__(self, width=800, height=480, caption="pygame"):
        self.width = width
        self.height = height
        self.caption = caption

    def init(self):
        # initialize pygame
        pygame.init()
        #  create a window
        screen = pygame.display.set_mode((self.width, self.height), pygame.SHOWN)
        pygame.display.set_caption(self.caption)
