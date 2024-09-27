import pygame
from pygame import SurfaceType
from pygame.font import Font

from classes.color import white


class ScoreCounter:
    def __init__(self, text: str, font: Font, color=white):
        self.text = text
        self.font = font
        self.color = color

    def draw(self, screen: SurfaceType, bounds: pygame.Rect, is_left: bool):
        score_surface = self.font.render(self.text, 1, self.color)
        score_rect = score_surface.get_rect()
        sign = -(int(is_left) * 2 - 1)
        score_rect.center = (
        bounds.width / 2 + (score_surface.get_width()/2 + 25) * sign, 12 + score_surface.get_height() / 2)
        screen.blit(score_surface, score_rect)
