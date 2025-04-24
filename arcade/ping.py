import os
import math
import pygame

from enum import Enum
from typing import Callable, List, Literal
from pygame.math import Vector2

from common.color import Color
from common.scene import Scene
from common.context import Context


path = os.path.dirname(os.path.realpath(__file__))


class Player(Enum):
    PLAYER_1 = 1
    PLAYER_2 = 2


class Paddle(pygame.Rect):
    speed: float = 5.0
    color: Color = Color.WHITE

    def __init__(self, x: int, y: int, width: int = 15, height: int = 150):
        super().__init__(0, 0, width, height)
        self.center = (x, y)

    def move_self(self, screen: pygame.Surface, dir: float):
        bound_dir = min(max(dir, -1.0), 1.0)

        self.y += int(bound_dir * self.speed)
        self.y = min(max(0, self.y), screen.get_height() - self.height)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color.rgb, self)


class Ball(pygame.Rect):
    speed: int = 10
    color: Color = Color.WHITE
    direction: Vector2

    on_collide_edge: Callable
    on_collide_paddle: Callable
    on_score: Callable

    def __init__(self, x: int, y: int, size: int = 10):
        super().__init__(0, 0, size, size)
        self.center = (x, y)
        self.direction = Vector2(1, 0).rotate(-180)

    def move_self(self, screen, left: Paddle, right: Paddle):
        self.x += int(self.direction.x * self.speed)
        self.y += int(self.direction.y * self.speed)

        # check right edge
        if self.right > screen.get_width():
            self.on_score(Player.PLAYER_1)

        # check left edge
        if self.left < 0:
            self.on_score(Player.PLAYER_2)

        # check top and bottom
        if self.bottom > screen.get_height() or self.top < 0:
            self.direction.y *= -1
            self.on_collide_edge()

        # check paddles
        def collide_paddle(paddle: Paddle, normal: Literal[-1, 1]):
            relative_collision = paddle.center[1] - self.center[1]
            normalized_relative_collision = relative_collision / (paddle.height / 2)
            bounce_angle = normalized_relative_collision * math.radians(-45)

            self.direction.x = math.cos(bounce_angle) * normal
            self.direction.y = math.sin(bounce_angle)

        if left.colliderect(self):
            self.on_collide_paddle(Player.PLAYER_1)
            collide_paddle(left, 1)

        if right.colliderect(self):
            self.on_collide_paddle(Player.PLAYER_2)
            collide_paddle(right, -1)

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color.rgb, self)


class Score:
    limit: int = 5
    current: List[int]

    font: pygame.font.Font
    color: Color = Color.WHITE

    def __init__(self):
        self.current = [0, 0]
        self.font: pygame.font.Font = pygame.font.SysFont("sansserif", 70)

    def get(self, player: Player):
        if player is Player.PLAYER_1:
            return self.current[0]
        elif player is Player.PLAYER_2:
            return self.current[1]

    def set(self, player: Player, value: int):
        match player:
            case Player.PLAYER_1:
                self.current[0] = value
            case Player.PLAYER_2:
                self.current[1] = value

    def draw(self, screen: pygame.Surface):
        for player in Player:
            text = self.font.render(str(self.get(player)), 1, self.color.rgb)
            rect = text.get_rect()

            match player:
                case Player.PLAYER_1:
                    sign = 1
                case Player.PLAYER_2:
                    sign = -1

            x_offset = (25 + text.get_width() // 2) * sign
            y_offset = 10 + text.get_height() // 2

            rect.center = (screen.get_width() // 2 + x_offset, y_offset)

            screen.blit(text, rect)


class Splash(Scene):
    background_color: Color = Color.BLACK
    image: pygame.Surface

    image_visible: bool = True
    wait_duration: int = 250

    start_time: int

    def start(self, context: Context):
        image_path = os.path.join(path, "..", "assets", "images", "insert.png")
        self.image = pygame.transform.scale(pygame.image.load(image_path), (256, 256))

        self.start_time = pygame.time.get_ticks()

    def update(self, context: Context):
        current_time = pygame.time.get_ticks()

        if current_time - self.start_time >= self.wait_duration:
            self.start_time = current_time
            self.image_visible = not self.image_visible

        self.draw(context.screen)

    def draw(self, screen: pygame.Surface):
        # clear screen
        screen.fill(self.background_color.rgb)

        # draw image
        rect = self.image.get_rect()
        rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 128)

        if self.image_visible:
            screen.blit(self.image, rect)

        # flip buffers
        pygame.display.flip()

    def on_event(self, context: Context, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                context.running = False
            if event.key == pygame.K_RETURN:
                context.scene = Game()


class Game(Scene):
    net_color: Color = Color.WHITE
    background_color: Color = Color.BLACK
    collision_sound: pygame.mixer.Sound

    ball: Ball
    left: Paddle
    right: Paddle
    score: Score

    def start(self, context: Context):
        screen = context.screen

        self.collision_sound = pygame.mixer.Sound(
            os.path.join(path, "..", "assets", "sounds", "ping1.wav")
        )

        self.left = Paddle(30, screen.get_height() // 2)
        self.right = Paddle(screen.get_width() - 30, screen.get_height() // 2)

        self.ball = Ball(screen.get_width() // 2, screen.get_height() // 2)

        def on_collide_edge():
            self.collision_sound.play()

        def on_collide_paddle(player: Player):
            self.collision_sound.play()

        def on_score(player: Player):
            self.score.set(player, self.score.get(player) + 1)

            match player:
                case Player.PLAYER_1:
                    direction = Vector2(-1, 0)
                case Player.PLAYER_2:
                    direction = Vector2(1, 0)

            self.ball.direction = direction
            self.ball.center = (screen.get_width() // 2, screen.get_height() // 2)

            if self.score.get(player) >= self.score.limit:
                print(f"Player {player.value} won!")
                context.scene = End(player)

        self.ball.on_collide_edge = on_collide_edge
        self.ball.on_collide_paddle = on_collide_paddle
        self.ball.on_score = on_score

        self.score = Score()

    def update(self, context: Context):
        screen = context.screen

        # move ball
        self.ball.move_self(screen, self.left, self.right)

        # move paddles
        keys = pygame.key.get_pressed()

        left_move_axis = keys[pygame.K_w] - keys[pygame.K_s]
        right_move_axis = keys[pygame.K_UP] - keys[pygame.K_DOWN]

        self.left.move_self(screen, -left_move_axis)
        self.right.move_self(screen, -right_move_axis)

        # draw the screen
        self.draw(screen)

    def draw(self, screen: pygame.Surface):
        # clear screen
        screen.fill(self.background_color.rgb)

        self.ball.draw(screen)
        self.left.draw(screen)
        self.right.draw(screen)
        self.score.draw(screen)

        # draw net
        dash_size = (1, 25)
        dash_count = 10

        for i in range(dash_count + 1):
            unit = screen.get_height() // dash_count

            rect = pygame.Rect((0, 0), dash_size)
            rect.center = (screen.get_width() // 2, unit * i)

            dash = pygame.draw.rect(screen, self.net_color.rgb, rect)

        # update screen
        pygame.display.flip()

    def on_event(self, context: Context, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                context.running = False


class End(Scene):
    font: pygame.font.Font
    text_color = Color.WHITE
    background_color = Color.BLACK

    def __init__(self, winner: Player):
        self.winner = winner

    def start(self, context: Context):
        self.font: pygame.font.Font = pygame.font.SysFont("sansserif", 70)

    def update(self, context: Context):
        context.screen.fill(self.background_color.rgb)

        text = self.font.render(
            f"Player {self.winner.value} wins!", 1, self.text_color.rgb
        )
        rect = text.get_rect()
        rect.center = (
            context.screen.get_width() // 2,
            context.screen.get_height() // 2,
        )

        context.screen.blit(text, rect)
        pygame.display.flip()

    def on_event(self, context: Context, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                context.running = False
            if event.key == pygame.K_RETURN:
                context.scene = Splash()


if __name__ == "__main__":
    context = Context(Splash())
