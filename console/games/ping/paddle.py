import pygame
from pygame import SurfaceType

from common.color import white
from common.controller import Controller


class Paddle:
    controller: Controller

    def __init__(
            self,
            controller: Controller,
            width=15,
            height=150,
            center=(0, 0),
            color=white,
            speed=300,
    ):
        self.speed = speed
        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = center
        self.color = color
        self.attach_controller(controller)

    def attach_controller(self, c: Controller):
        self.controller = c

    def move(self, delta_time: float, bounds: pygame.Rect):
        # Up
        if self.rect.top > bounds.top:
            if self.controller.dpad.up is True:  # or player.joystick.y >= DEAD_ZONE:
                self.rect.y -= self.speed * delta_time
        # Down
        if self.rect.bottom < bounds.bottom:
            if self.controller.dpad.down is True:  # or player.joystick.y <= DEAD_ZONE:
                self.rect.y += self.speed * delta_time

    def draw(self, screen: SurfaceType):
        pygame.draw.rect(screen, self.color, self.rect)
