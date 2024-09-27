import pygame
from pygame.font import Font
from pygame.mixer import SoundType

from classes import color
from classes.color import black
from classes.controller import Controller
from games.ping.background import Background
from games.ping.ball import Ball
from games.ping.paddle import Paddle
from games.ping.score_counter import ScoreCounter
from games.ping.state import State, Running, Ended
from systems import emulator
from systems.context import Context


class Game:
    player_1: Controller
    player_2: Controller

    ball: Ball
    paddles: [Paddle]
    bounds: (int, int)
    state: State

    score_font: Font
    collision_sound: SoundType

    def __init__(self, p1: Controller, p2: Controller):
        self.player_1 = p1
        self.player_2 = p2

    def start(self):
        self.ball = Ball(center=(width / 2, height / 2))
        self.paddles = [
            Paddle(controller=self.player_1, center=(30, height / 2)),
            Paddle(controller=self.player_2, center=(width - 30, height / 2))
        ]

        self.bounds = pygame.Rect(0, 0, width, height)
        self.bounds.center = (width / 2, height / 2)

        self.state = Running()

        # load resources
        self.score_font = pygame.font.SysFont("sansserif", 70)
        self.collision_sound = pygame.mixer.Sound('sounds/ping1.wav')

        loop = ctx.run(self.update)
        loop()

    def update(self):
        # define callbacks
        def on_collide():
            self.collision_sound.play()

        def on_score(scorer):
            self.state.scores[scorer] += 1

        def on_win_detected(winner):
            self.state = Ended(winner)

        # logic
        match self.state:
            case Running():
                # move elements
                self.paddles[0].move(ctx.dt, self.bounds)
                self.paddles[1].move(ctx.dt, self.bounds)
                self.ball.move(ctx.dt, self.bounds, self.paddles, on_collide, on_score)
                # check score
                self.state.check_score(on_win_detected)

        # draw
        self.draw()

        emulator.update(player_1, False)
        emulator.update(player_2, True)

    def draw(self):
        match self.state:
            case Running(scores=scores):
                # draw background
                Background().draw(screen, width)
                # draw ball
                self.ball.draw(screen)
                # draw paddles
                for p in self.paddles:
                    p.draw(screen)
                # draw score
                ScoreCounter(str(scores[0]), self.score_font).draw(screen, self.bounds, True)
                ScoreCounter(str(scores[1]), self.score_font).draw(screen, self.bounds, False)
            case Ended(winner=winner):
                # draw background
                screen.fill(black)
                draw_text = self.score_font.render(f"Player {winner + 1} WINS!", 1, color.white)
                screen.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))
            case _:
                print(self.state)

        # flip buffers
        pygame.display.flip()

    pass


if __name__ == "__main__":
    ctx = Context(caption="ping", framerate=60)
    screen = ctx.screen
    width = ctx.width
    height = ctx.height

    player_1 = Controller()
    player_2 = Controller()

    game = Game(player_1, player_2)
    game.start()
