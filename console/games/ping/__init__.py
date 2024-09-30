import pygame
from pygame.font import Font
from pygame.mixer import SoundType

from common import color
from common.color import black
from common.controller import Controller
from console.games.ping.background import Background
from console.games.ping.ball import Ball
from console.games.ping.paddle import Paddle
from console.games.ping.score_counter import ScoreCounter
from console.games.ping.state import State, Running, Ended
from common.context import Context


class Game:
    player_1: Controller
    player_2: Controller

    ball: Ball
    paddles: [Paddle]
    bounds: (int, int)
    state: State

    score_font: Font
    collision_sound: SoundType

    def __init__(self, ctx: Context, p1: Controller, p2: Controller):
        self.ctx = ctx
        self.player_1 = p1
        self.player_2 = p2

    def start(self):
        self.ball = Ball(center=(self.ctx.width / 2, self.ctx.height / 2))
        self.paddles = [
            Paddle(controller=self.player_1, center=(30, self.ctx.height / 2)),
            Paddle(controller=self.player_2, center=(self.ctx.width - 30, self.ctx.height / 2))
        ]

        self.bounds = pygame.Rect(0, 0, self.ctx.width, self.ctx.height)
        self.bounds.center = (self.ctx.width / 2, self.ctx.height / 2)

        self.state = Running()

        # load resources
        self.score_font = pygame.font.SysFont("sansserif", 70)
        # self.collision_sound = pygame.mixer.Sound('sounds/ping1.wav')

        loop = self.ctx.run(self.update)
        loop()

    def update(self):
        # define callbacks
        def on_collide():
            # self.collision_sound.play()
            pass

        def on_score(scorer):
            self.state.scores[scorer] += 1

        def on_win_detected(winner):
            self.state = Ended(winner)

        # logic
        match self.state:
            case Running():
                # move elements
                self.paddles[0].move(self.ctx.dt, self.bounds)
                self.paddles[1].move(self.ctx.dt, self.bounds)
                self.ball.move(self.ctx.dt, self.bounds, self.paddles, on_collide, on_score)
                # check score
                self.state.check_score(on_win_detected)

        # draw
        self.draw()

    def draw(self):
        match self.state:
            case Running(scores=scores):
                # draw background
                Background().draw(self.ctx.screen, self.ctx.width)
                # draw ball
                self.ball.draw(self.ctx.screen)
                # draw paddles
                for p in self.paddles:
                    p.draw(self.ctx.screen)
                # draw score
                ScoreCounter(str(scores[0]), self.score_font).draw(self.ctx.screen, self.bounds, True)
                ScoreCounter(str(scores[1]), self.score_font).draw(self.ctx.screen, self.bounds, False)
            case Ended(winner=winner):
                # draw background
                self.ctx.screen.fill(black)
                text = f"Player {winner + 1} WINS!"
                text_surface = self.score_font.render(text, 1, color.white)
                self.ctx.screen.blit(
                    text_surface,
                    (self.ctx.width / 2 - text_surface.get_width() / 2,
                     self.ctx.height / 2 - text_surface.get_height() / 2)
                )
            case _:
                print(self.state)

        # flip buffers
        pygame.display.flip()

    pass


if __name__ == "__main__":
    context = Context(caption="ping", framerate=60)

    player_1 = Controller()
    player_2 = Controller()

    game = Game(context, player_1, player_2)
    game.start()
