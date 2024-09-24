import math

import pygame
from pygame import Vector2


class Ball:
    def __init__(
        self,
        speed = 10,
        direction: Vector2 = Vector2(-1, 0),
        center = (0, 0),
        size: int = 10,
        color = (255, 255, 255)
    ):
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(0, 0, size, size)
        self.rect.center = center
        self.color = color

    def move(self, paddles, screen_width, screen_height, on_collide=lambda: None, on_score=lambda i: None):
        # Collisions
        # Side walls
        if self.rect.right > screen_width:
            # Left Player Scored!
            on_score(0)

            self.direction = Vector2(-1, 0)
            self.rect.center = (screen_width / 2, screen_height / 2)
            # Send haptic feedback
            # asyncio.run(send_to_all_clients('300'))

        if self.rect.left < 0:
            # Right Player Scored!
            on_score(1)

            self.direction = Vector2(1, 0)
            self.rect.center = (screen_width / 2, screen_height / 2)
            # asyncio.run(send_to_all_clients('300'))

        if self.rect.bottom > screen_height or self.rect.top < 0:
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

                # Send HF
                # asyncio.run(send_to_all_clients('100'))

            sign = sign * -1

        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
