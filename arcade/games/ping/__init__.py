import pygame

from classes import color
from classes.color import black
from classes.controller import Controller
from systems import emulator
from systems.context import game_loop

if __name__ == "__main__":
    # initialize pygame
    width = 700
    height = 500
    bounds = pygame.Rect(0, 0, width, height)
    bounds.center = (width / 2, height / 2)
    pygame.init()
    screen_size = (width, height)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("ping")

from games.ping.ball import Ball
from games.ping.paddle import Paddle
from games.ping.game_logic import State, Running, Ended, Game
from games.ping.background import Background
from games.ping.score_counter import ScoreCounter

# load resources
score_font = pygame.font.SysFont("sansserif", 70)
COLLISION_SOUND = pygame.mixer.Sound('sounds/ping1.wav')


def draw(ball: Ball, paddles: [Paddle], game: Game):
    match game.state:
        case Running(scores=scores):
            # draw background
            Background().draw(screen, width)
            # draw ball
            ball.draw(screen)
            # draw paddles
            for paddle in paddles:
                paddle.draw(screen)
            # draw score
            ScoreCounter(str(game.state.scores[0]), score_font).draw(screen, bounds, True)
            ScoreCounter(str(game.state.scores[1]), score_font).draw(screen, bounds, False)
        case Ended(winner=winner):
            # draw background
            screen.fill(black)
            draw_text = score_font.render(f"Player {winner + 1} WINS!", 1, color.white)
            screen.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))
        case _:
            print(game.state)

    # flip buffers
    pygame.display.flip()


def start(player_1, player_2):
    game = Game()
    ball = Ball(center=(width / 2, height / 2))
    paddles = [
        Paddle(center=(30, height / 2)),
        Paddle(center=(width - 30, height / 2))
    ]

    update(player_1, player_2, paddles, ball, game)


@game_loop
def update(player_1, player_2, paddles, ball: Ball, game: Game):
    # define callbacks
    def on_collide():
        COLLISION_SOUND.play()

    def on_score(i):
        game.state.scores[i] += 1

    def on_win_detected(i):
        game.state = Ended(i)

    # logic
    match game.state:
        case Running():
            # move elements
            paddles[0].move(player_1, bounds)
            paddles[1].move(player_2, bounds)
            ball.move(paddles, bounds, on_collide, on_score)
            # check score
            game.state.check_score(on_win_detected)

    # draw
    draw(ball, paddles, game)

    emulator.update(player_1)
    emulator.update(player_2, True)


if __name__ == "__main__":
    player_1 = Controller()
    player_2 = Controller()

    # start the game
    start(player_1, player_2)
