import pygame

from .scene import Scene


class Context:
    _scene: Scene
    screen: pygame.Surface

    running: bool

    @property
    def scene(self):
        return self._scene

    @scene.setter
    def scene(self, value):
        value.close(self)
        self._scene = value
        value.start(self)

    def __init__(self, scene: Scene):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800, 480))
        self.clock = pygame.time.Clock()

        self.scene = scene
        scene.start(self)

        self.running = True
        while self.running:
            self.clock.tick(60)
            for event in pygame.event.get():
                self.scene.on_event(self, event)
                if event.type == pygame.QUIT:
                    self.running = False

            self.scene.update(self)

        pygame.quit()
