import pygame
import math
from pygame.math import Vector2

from classes import color
from classes.controller import Controller

player1 = Controller()
player2 = Controller()

if __name__ == "__main__":
    # initialize pygame
    width = 700
    height = 500
    pygame.init()
    screen_size = (width, height)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("ping")

# Dead zone
DEAD_ZONE = 0.2

# Font
SCORE_FONT = pygame.font.SysFont("sansserif", 70)

# Left paddle properties
LEFT_PADDLE_WIDTH = 15
LEFT_PADDLE_HEIGHT = 150
LEFT_PADDLE_SPEED = 5

# Right paddle properties
RIGHT_PADDLE_WIDTH = 15
RIGHT_PADDLE_HEIGHT = 150
RIGHT_PADDLE_SPEED = 5

# Ball properties
BALL_WIDTH = 10
BALL_HEIGHT = 10
BALL_SPEED = 10
BALL_DIR = (Vector2(1, 0)).rotate(180)

SCORE_LIMIT = 5

COLLISION_SOUND = pygame.mixer.Sound('sounds/ping1.wav')


def draw(ball, left_paddle, right_paddle, score):
    # clear screen
    screen.fill((0, 0, 0))

    # draw ball
    pygame.draw.rect(screen, (255, 255, 255), ball)

    # draw paddles
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)

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


def move_paddle(left_paddle, player):
    # Up
    if left_paddle.top > 0:
        if player.dpad.up is True or player.joystick.y >= DEAD_ZONE:
            left_paddle.y -= LEFT_PADDLE_SPEED
    # Down
    elif left_paddle.bottom < height:
        if player.dpad.down is True or player.joystick.y <= DEAD_ZONE:
            left_paddle.y += LEFT_PADDLE_SPEED


def move_ball(ball, left_paddle, right_paddle, score):
    global BALL_DIR

    # Collisions
    # Side walls
    if ball.right > width:
        # Left Player Scored!
        score[0] += 1

        BALL_DIR = Vector2(-1, 0)
        ball.center = (width / 2, height / 2)
        # Send haptic feedback
        # asyncio.run(send_to_all_clients('300'))

    if ball.left < 0:
        # Left Player Scored!
        score[1] += 1

        BALL_DIR = Vector2(1, 0)
        ball.center = (width / 2, height / 2)
        # asyncio.run(send_to_all_clients('300'))

    if ball.bottom > height or ball.top < 0:
        COLLISION_SOUND.play()
        BALL_DIR.y *= -1

    # Paddles
    if left_paddle.colliderect(ball):
        COLLISION_SOUND.play()
        relative_collision = left_paddle.centery - ball.centery

        normalized_relative_collision = (relative_collision / (LEFT_PADDLE_HEIGHT / 2))

        bounce_angle = normalized_relative_collision * math.radians(-60)

        BALL_DIR.x = math.cos(bounce_angle)
        BALL_DIR.y = math.sin(bounce_angle)

        # Send HF
        # asyncio.run(send_to_all_clients('100'))

    if right_paddle.colliderect(ball):
        COLLISION_SOUND.play()
        relative_collision = right_paddle.centery - ball.centery

        normalized_relative_collision = (relative_collision / (RIGHT_PADDLE_HEIGHT / 2))

        bounce_angle = normalized_relative_collision * math.radians(-60)

        BALL_DIR.x = -math.cos(bounce_angle)
        BALL_DIR.y = math.sin(bounce_angle)

        # Send HF
        # asyncio.run(send_to_all_clients('100'))

    ball.x += BALL_DIR.x * BALL_SPEED
    ball.y += BALL_DIR.y * BALL_SPEED


def draw_winner(text):
    draw_text = SCORE_FONT.render(text, 1, color.white)

    screen.blit(draw_text, (width / 2 - draw_text.get_width() / 2, height / 2 - draw_text.get_height() / 2))

    pygame.display.flip()
    pygame.time.delay(5000)


def main():
    ball = pygame.Rect(width / 2, height / 2, BALL_WIDTH, BALL_HEIGHT)
    ball.center = (width / 2, height / 2)

    left_paddle = pygame.Rect(0, 0, LEFT_PADDLE_WIDTH, LEFT_PADDLE_HEIGHT)
    left_paddle.center = (30, height / 2)

    right_paddle = pygame.Rect(0, 0, RIGHT_PADDLE_WIDTH, RIGHT_PADDLE_HEIGHT)
    right_paddle.center = (width - 30, height / 2)

    score = [0, 0]
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        move_paddle(left_paddle, player1)
        move_paddle(right_paddle, player2)

        move_ball(ball, left_paddle, right_paddle, score)

        draw(ball, left_paddle, right_paddle, score)

        if score[0] >= SCORE_LIMIT:
            score[0] += 1
            draw_winner('PLAYER 1 WINS!')
            return

        if score[1] >= SCORE_LIMIT:
            score[1] += 1
            draw_winner('PLAYER 2 WINS!')
            return

    pygame.quit()


if __name__ == "__main__":
    # start the game
    main()
