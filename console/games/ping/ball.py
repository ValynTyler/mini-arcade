import math

import pygame
from pygame import Vector2


class Ball:
    def __init__(
            self,
            speed=600,
            direction: Vector2 = Vector2(-1, 0),
            center=(0, 0),
            size: int = 10,
            color=(255, 255, 255)
    ):
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.center = center
        self.color = color

    def move(self, delta_time: float, bounds: pygame.Rect, paddles, on_collide=lambda: None, on_score=lambda i: None):
        # Collisions
        # Left
        if self.rect.right > bounds.right:
            # Left Player Scored!
            on_score(0)
            self.direction = Vector2(-1, 0)
            self.rect.center = (bounds.centerx, bounds.centery)
        # Right
        if self.rect.left < bounds.left:
            # Right Player Scored!
            on_score(1)
            self.direction = Vector2(1, 0)
            self.rect.center = (bounds.centerx, bounds.centery)
        # Top and Bottom
        if self.rect.bottom > bounds.bottom or self.rect.top < bounds.top:
            on_collide()
            self.direction.y *= -1

        # Paddles
        sign = 1
        for paddle in paddles:
            if paddle.rect.colliderect(self.rect):
                on_collide()
                relative_collision = paddle.rect.centery - self.rect.centery
                normalized_relative_collision = (relative_collision / (paddle.rect.height / 2))
                bounce_angle = normalized_relative_collision * math.radians(-60)

                self.direction.x = math.cos(bounce_angle) * sign
                self.direction.y = math.sin(bounce_angle)

            sign = sign * -1

        # Move ball
        self.direction.normalize()
        self.rect.x += self.direction.x * self.speed * delta_time
        self.rect.y += self.direction.y * self.speed * delta_time

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
