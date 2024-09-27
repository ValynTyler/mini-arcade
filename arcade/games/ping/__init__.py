import pygame

from classes import color
from classes.color import black
from classes.controller import Controller
from systems import emulator
from systems.context import Context

if __name__ == "__main__":
    ctx = Context(caption="ping", framerate=60)
    screen = ctx.screen
    width = ctx.width
    height = ctx.height

from games.ping.ball import Ball
from games.ping.paddle import Paddle
from games.ping.state import State, Running, Ended
from games.ping.background import Background
from games.ping.score_counter import ScoreCounter

# load resources
score_font = pygame.font.SysFont("sansserif", 70)
COLLISION_SOUND = pygame.mixer.Sound('sounds/ping1.wav')


class Game:
    player_1: Controller
    player_2: Controller

    ball: Ball
    paddles: [Paddle]
    bounds: (int, int)
    state: State

    def __init__(self, p1: Controller, p2: Controller):
        self.player_1 = p1
        self.player_2 = p2

    def start(self):
        self.ball = Ball(center=(width / 2, height / 2))
        self.paddles = [
            Paddle(center=(30, height / 2)),
            Paddle(center=(width - 30, height / 2))
        ]

        self.bounds = pygame.Rect(0, 0, width, height)
        self.bounds.center = (width / 2, height / 2)

        self.state = Running()

        loop = ctx.run(self.update)
        loop()

    def update(self):
        # define callbacks
        def on_collide():
            COLLISION_SOUND.play()

        def on_score(i):
            self.state.scores[i] += 1

        def on_win_detected(i):
            self.state = Ended(i)

        # logic
        match self.state:
            case Running():
                # move elements
                self.paddles[0].move(ctx.dt, player_1, self.bounds)
                self.paddles[1].move(ctx.dt, player_2, self.bounds)
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
                ScoreCounter(str(scores[0]), score_font).draw(screen, self.bounds, True)
                ScoreCounter(str(scores[1]), score_font).draw(screen, self.bounds, False)
            case Ended(winner=winner):
                # draw background
                screen.fill(black)
                draw_text = score_font.render(f"Player {winner + 1} WINS!", 1, color.white)
                screen.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))
            case _:
                print(self.state)

        # flip buffers
        pygame.display.flip()

    pass


if __name__ == "__main__":
    player_1 = Controller()
    player_2 = Controller()

    game = Game(player_1, player_2)
    game.start()
