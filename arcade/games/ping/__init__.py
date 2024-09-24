import pygame
from pygame.examples.aliens import SCORE

from classes import color
from classes.controller import Controller
from systems import emulator
from systems.context import game_loop

if __name__ == "__main__":
    # initialize pygame
    width = 700
    height = 500
    bounds = pygame.Rect(0, 0, width, height)
    bounds.center = (width/2, height/2)
    pygame.init()
    screen_size = (width, height)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("ping")

from games.ping.ball import Ball
from games.ping.paddle import Paddle
from games.ping.state import State
from games.ping.background import Background
from games.ping.score_counter import ScoreCounter

# load resources
score_font = pygame.font.SysFont("sansserif", 70)
COLLISION_SOUND = pygame.mixer.Sound('sounds/ping1.wav')


def draw(ball: Ball, paddles: [Paddle], state: State):
    # draw background
    Background().draw(screen, width)

    # draw ball
    ball.draw(screen)

    # draw paddles
    for paddle in paddles:
        paddle.draw(screen)

    # draw score
    ScoreCounter(str(state.current.score[0]), score_font).draw(screen, bounds, True)
    ScoreCounter(str(state.current.score[1]), score_font).draw(screen, bounds, False)

    # flip buffers
    pygame.display.flip()


def draw_winner(text):
    draw_text = score_font.render(text, 1, color.white)

    screen.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))

    pygame.display.flip()
    pygame.time.delay(5000)


def main(player_1, player_2):
    state = State()
    ball = Ball(center=(width / 2, height / 2))
    paddles = [
        Paddle(center=(30, height / 2)),
        Paddle(center=(width - 30, height / 2))
    ]

    run(player_1, player_2, paddles, ball, state)


def update(player_1, player_2, paddles, ball: Ball, state):
    # define callbacks
    def on_collide():
        COLLISION_SOUND.play()

    def on_score(i):
        state.current.score[i] += 1

    # move elements
    paddles[0].move(player_1, bounds)
    paddles[1].move(player_2, bounds)
    ball.move(paddles, bounds, on_collide, on_score)

    # draw
    draw(ball, paddles, state)

    # check score
    # if score[0] >= SCORE_LIMIT:
    #     score[0] += 1
    #     draw_winner('PLAYER 1 WINS!')
    #     return
    #
    # if score[1] >= SCORE_LIMIT:
    #     score[1] += 1
    #     draw_winner('PLAYER 2 WINS!')
    #     return


@game_loop
def run(player_1, player_2, paddles, ball, state):
    emulator.update(player_1)
    emulator.update(player_2, True)
    update(player_1, player_2, paddles, ball, state)


# if file is launched, run with emulated controls
if __name__ == "__main__":
    player1 = Controller()
    player2 = Controller()

    # start the game
    main(player1, player2)
