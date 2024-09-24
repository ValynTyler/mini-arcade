import pygame

from classes import color
from classes.controller import Controller
from systems import emulator
from systems.context import game_loop

if __name__ == "__main__":
    # initialize pygame
    width = 700
    height = 500
    pygame.init()
    screen_size = (width, height)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("ping")

from games.ping.ball import Ball
from games.ping.paddle import Paddle

# load resources
SCORE_FONT = pygame.font.SysFont("sansserif", 70)
COLLISION_SOUND = pygame.mixer.Sound('sounds/ping1.wav')

SCORE_LIMIT = 5


def draw(ball: Ball, paddles, score):
    # clear screen
    screen.fill(color.black)

    # draw ball
    pygame.draw.rect(screen, (255, 255, 255), ball.rect)

    # draw paddles
    for paddle in paddles:
        pygame.draw.rect(screen, paddle.color, paddle.rect)

    # draw border
    dot_size = (1, 25)
    for x in range(10):
        pygame.draw.rect(screen, (255, 255, 255), ((width / 2 + dot_size[0] / 2, x * 50), dot_size))

    # draw score
    # left
    left_score_text = SCORE_FONT.render(f"{score[0]}", 1, (255, 255, 255))
    left_score_text_rect = left_score_text.get_rect()
    left_score_text_rect.topleft = (width / 2 - left_score_text.get_width() - 25, 10)
    screen.blit(left_score_text, left_score_text_rect)

    # right
    right_score_text = SCORE_FONT.render(f"{score[1]}", 1, (255, 255, 255))
    right_score_text_rect = right_score_text.get_rect()
    right_score_text_rect.topright = (width / 2 + right_score_text.get_width() + 25, 10)
    screen.blit(right_score_text, right_score_text_rect)

    # flip buffers
    pygame.display.flip()


def draw_winner(text):
    draw_text = SCORE_FONT.render(text, 1, color.white)

    screen.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))

    pygame.display.flip()
    pygame.time.delay(5000)


def main(player_1, player_2):
    ball = Ball(center=(width / 2, height / 2))
    paddles = [
        Paddle(center=(30, height / 2)),
        Paddle(center=(width - 30, height / 2))
    ]

    score = [0, 0]
    run(player_1, player_2, paddles, ball, score)


def update(player_1, player_2, paddles, ball, score):
    # define callbacks
    def on_collide():
        COLLISION_SOUND.play()
    def on_score(i):
        score[i] += 1

    # move elements
    paddles[0].move(player_1, height)
    paddles[1].move(player_2, height)
    ball.move(paddles, width, height, on_collide, on_score)

    # draw
    draw(ball, paddles, score)

    # check score
    if score[0] >= SCORE_LIMIT:
        score[0] += 1
        draw_winner('PLAYER 1 WINS!')
        return

    if score[1] >= SCORE_LIMIT:
        score[1] += 1
        draw_winner('PLAYER 2 WINS!')
        return


@game_loop
def run(player_1, player_2, paddles, ball, score):
    emulator.update(player_1)
    emulator.update(player_2, True)
    update(player_1, player_2, paddles, ball, score)


if __name__ == "__main__":
    player1 = Controller()
    player2 = Controller()

    # start the game
    main(player1, player2)
