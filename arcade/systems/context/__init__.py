import pygame


def game_loop(func):
    def inner(*args, **kwargs):
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            # run lambda
            func(*args, **kwargs)
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
    return inner
