import pygame

from classes.controller import Controller
from classes.color import white

class Paddle:
    def __init__(
        self,
        width = 15,
        height = 150,
        center = (0, 0),
        color = white,
        speed = 5,
    ):
        self.speed = speed
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center
        self.color = color

    def move(self, inputs: Controller, screen_height):
        # Up
        if self.rect.top > 0:
            if inputs.dpad.up is True:  # or player.joystick.y >= DEAD_ZONE:
                self.rect.y -= self.speed
        # Down
        if self.rect.bottom < screen_height:
            if inputs.dpad.down is True:  # or player.joystick.y <= DEAD_ZONE:
                self.rect.y += self.speed
