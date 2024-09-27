import pygame
from pygame import SurfaceType


class Context:
    screen: SurfaceType
    running: bool
    dt: float

    def __init__(self, width=800, height=480, caption="pygame", framerate: int = 60):
        self.width = width
        self.height = height
        self.caption = caption
        self.framerate = framerate
        self.init()

    def init(self):
        # initialize pygame
        pygame.init()
        #  create a window
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.SHOWN)
        pygame.display.set_caption(self.caption)

    def run(self, func):
        def inner(*args, **kwargs):
            clock = pygame.time.Clock()
            self.running = True
            while self.running:
                self.dt = clock.tick(self.framerate) / 1000
                # run lambda
                func(*args, **kwargs)
                # events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
        return inner
