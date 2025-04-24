import pygame.event


class Scene:
    def start(self, context):
        pass

    def update(self, context):
        pass

    def close(self, context):
        pass

    def on_event(self, context, event: pygame.event.Event):
        pass
