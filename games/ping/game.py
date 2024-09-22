import pygame
import math
from pygame.math import Vector2

if __name__ == "__main__":
    # initialize pygame
    pygame.init()
    screen_size = (700, 500)
    #  create a window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("ping")

# Font
SCORE_FONT = pygame.font.SysFont("sansserif", 70)

# Left paddel properties
LEFT_PADDLE_WIDTH = 15
LEFT_PADDLE_HEIGHT = 150
LEFT_PADDLE_SPEED = 5

# Right paddel properties
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
    #clear screen
    screen.fill((0, 0, 0))

    # draw ball
    pygame.draw.rect(screen, (255, 255, 255), ball)

    # draw paddels
    pygame.draw.rect(screen, (255, 255, 255), left_paddle)
    pygame.draw.rect(screen, (255, 255, 255), right_paddle)

    # draw border
    dot_size = (1, 25)
    for x in range(10):
        pygame.draw.rect(screen, (255, 255, 255), ((WIDTH/2 + dot_size[0]/2, x * 50), dot_size))

    # draw score
    # left
    left_score_text = SCORE_FONT.render(f"{score[0]}", 1, (255, 255, 255))
    left_score_text_rect = left_score_text.get_rect()
    left_score_text_rect.topleft = (WIDTH/2 - left_score_text.get_width() - 25, 10)
    screen.blit(left_score_text, left_score_text_rect)
    
    #right
    right_score_text = SCORE_FONT.render(f"{score[1]}", 1, (255, 255, 255))
    right_score_text_rect = right_score_text.get_rect()
    right_score_text_rect.topright = (WIDTH/2 + right_score_text.get_width() + 25, 10)
    screen.blit(right_score_text, right_score_text_rect)

    # flip buffers
    pygame.display.flip()

def movePaddels(lpad, rpad):
    # Left Paddle
    # Left Paddle Up
    if lpad.top > 0 and PLAYER_1.dpad.up == 0:
        lpad.y -= LEFT_PADDLE_SPEED
    # Left Paddle Down
    elif lpad.bottom < HEIGHT and PLAYER_1.dpad.down == 0:
        lpad.y += LEFT_PADDLE_SPEED
    # Joystick
    elif PLAYER_1.joystick.y >= 0 and lpad.bottom < HEIGHT:
        lpad.y += PLAYER_1.joystick.y * LEFT_PADDLE_SPEED
    elif PLAYER_1.joystick.y < 0 and lpad.top > 0:
        lpad.y += PLAYER_1.joystick.y * LEFT_PADDLE_SPEED
                
    # Right Paddle
    # Right Paddle Up
    if rpad.top > 0 and PLAYER_2.dpad.up == 0:
        rpad.y -= RIGHT_PADDLE_SPEED
    # Right Paddle Down
    elif rpad.bottom < HEIGHT and PLAYER_2.dpad.down == 0:
        rpad.y += RIGHT_PADDLE_SPEED
    # Joystick
    elif PLAYER_2.joystick.y >= 0 and rpad.bottom < HEIGHT:
        rpad.y += PLAYER_2.joystick.y * RIGHT_PADDLE_SPEED
    elif PLAYER_2.joystick.y <= 0 and rpad.top > 0:
        rpad.y += PLAYER_2.joystick.y * RIGHT_PADDLE_SPEED
    
def moveBall(ball, lpad, rpad, score):
    global BALL_DIR

    # Collisions
    # Side walls
    if ball.right > WIDTH:
        # Left Player Scored!
        score[0] += 1

        BALL_DIR = Vector2(-1, 0)
        ball.center = (WIDTH/2, HEIGHT/2)
        # Send haptic feedback
        asyncio.run(send_to_all_clients('300'))

    if ball.left < 0:
        # Left Player Scored!
        score[1] += 1

        BALL_DIR = Vector2(1, 0)
        ball.center = (WIDTH/2, HEIGHT/2)
        asyncio.run(send_to_all_clients('300'))

    if ball.bottom > HEIGHT or ball.top < 0:
        COLLISION_SOUND.play()
        BALL_DIR.y *= -1

    # Paddles
    if lpad.colliderect(ball):
        COLLISION_SOUND.play()
        relative_collision = (lpad.y + (LEFT_PADDLE_HEIGHT/2)) - ball.y;

        normalized_relative_collision = (relative_collision / (LEFT_PADDLE_HEIGHT/2));

        bounce_angle = normalized_relative_collision * math.radians(-60);

        BALL_DIR.x = math.cos(bounce_angle);
        BALL_DIR.y = math.sin(bounce_angle)

        # Send HF
        asyncio.run(send_to_all_clients('100'))

    if rpad.colliderect(ball):
        COLLISION_SOUND.play()
        relative_collision = (rpad.y + (RIGHT_PADDLE_HEIGHT/2)) - ball.y;

        normalized_relative_collision = (relative_collision / (RIGHT_PADDLE_HEIGHT/2));
        
        bounce_angle = normalized_relative_collision *  math.radians(-60);

        BALL_DIR.x = -math.cos(bounce_angle);
        BALL_DIR.y = math.sin(bounce_angle);
    
        # Send HF
        asyncio.run(send_to_all_clients('100'))

    ball.x += BALL_DIR.x * BALL_SPEED  
    ball.y += BALL_DIR.y * BALL_SPEED

def draw_winner(text):
    draw_text = SCORE_FONT.render(text, 1, WHITE)

    screen.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))

    pygame.display.flip()
    pygame.time.delay(5000)

def main():
    # Splash screen
    show_splash_text = True
    on_splash_screen = True
    while on_splash_screen:
        for event in pygame.event.get():
            # Detect [x] or alt + f4
            if event.type == pygame.QUIT: running = False
            # Detect payment
            if event.type == SENSOR_ACTIVATED:
                print('Inserted coin successfully')
                on_splash_screen = False
            # Return to menu
            if event.type == BUTTON_PRESSED:
                print('Returned to Menu')
                return
            # Timer
            if event.type == TIMER_EVENT:
                show_splash_text = not show_splash_text
            # Return to menu
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    print('Returned to Menu')
                    return
                if event.key == pygame.K_LSHIFT:
                    print('Inserted coin successfully')
                    on_splash_screen = False

            if event.type == BUTTON_PRESSED:
                print('Returned to Menu')
                return
            
            if event.type == SENSOR_ACTIVATED:
                print('Inserted coin successfully')
                on_splash_screen = False
                
        # Draw
        # Background
        screen.fill(BLACK)
        # Splash text
        if show_splash_text:
            screen.blit(INSERT_TEXT, (WIDTH//2 - 128, HEIGHT//2))
        # Flip buffers
        pygame.display.flip()

        # Keep polling menu button
        update_menu_button()

        # Refresh pin readout
        update_pins()

    ball = pygame.Rect(WIDTH/2, HEIGHT/2, BALL_WIDTH, BALL_HEIGHT)

    left_paddle = pygame.Rect(0, 0, LEFT_PADDLE_WIDTH, LEFT_PADDLE_HEIGHT)
    left_paddle.center = (30, HEIGHT/2)
    right_paddle = pygame.Rect(0, 0, RIGHT_PADDLE_WIDTH, RIGHT_PADDLE_HEIGHT)
    right_paddle.center = (WIDTH - 30, HEIGHT/2)

    score = [0, 0]
    
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    print('Returned to Menu')
                    return
            if event.type == BUTTON_PRESSED:
                print('Returned to Menu')
                return
                
        movePaddels(left_paddle, right_paddle)
        moveBall(ball, left_paddle, right_paddle, score)
        
        draw(ball, left_paddle, right_paddle, score)

        if score[0] >= SCORE_LIMIT:
            score[0] += 1
            draw_winner('PLAYER 1 WINS!')
            return
        
        if score[1] >= SCORE_LIMIT:
            score[1] += 1
            draw_winner('PLAYER 2 WINS!')
            return
        
        # Keep polling menu button
        update_menu_button()

        # Refresh pin readout
        update_pins()
        # Read button
        if BUTTON_PIN != BUTTON_PIN_LF:
            print('Returned to Menu')
            return

    pygame.quit()

if __name__ == "__main__":
    # start the game
    main()