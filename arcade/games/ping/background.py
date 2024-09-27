import pygame
from pygame import SurfaceType

from classes.color import black, white


class Background:
    def __init__(self, background_color=black, border_color=white):
        self.background_color = background_color
        self.border_color = border_color

    def draw(self, screen: SurfaceType, screen_width):
        screen.fill(self.background_color)

        # draw border
        dot_size = (1, 25)
        for x in range(10):
            pygame.draw.rect(screen, self.border_color, ((screen_width / 2 + dot_size[0] / 2, x * 50), dot_size))
