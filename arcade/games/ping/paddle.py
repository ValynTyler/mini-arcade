import pygame
from pygame import SurfaceType

from classes.controller import Controller
from classes.color import white

class Paddle:
    def __init__(
        self,
        width = 15,
        height = 150,
        center = (0, 0),
        color = white,
        speed = 300,
    ):
        self.speed = speed
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center
        self.color = color

    def move(self, delta_time: float, inputs: Controller, bounds: pygame.Rect):
        # Up
        if self.rect.top > bounds.top:
            if inputs.dpad.up is True:  # or player.joystick.y >= DEAD_ZONE:
                self.rect.y -= self.speed * delta_time
        # Down
        if self.rect.bottom < bounds.bottom:
            if inputs.dpad.down is True:  # or player.joystick.y <= DEAD_ZONE:
                self.rect.y += self.speed * delta_time

    def draw(self, screen: SurfaceType):
        pygame.draw.rect(screen, self.color, self.rect)
