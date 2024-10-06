import pygame
from button import Button
from settings import RED


class Window:
    def __init__(self, resolution, background_color, caption):
        pygame.init()
        self.resolution = resolution
        self.window = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)
        self.window.fill(background_color)
        self.buttons = []
        self.create_buttons()
        pygame.display.update()

    def create_buttons(self):
        for y in range(3):
            for x in range(3):
                self.buttons.append(Button(80, 80, x, y, self.window))

    def on_click(self, position):
        for button in self.buttons:
            result = button.on_click(position)
            if result:
                return result

    def on_ai_move(self, x, y):
        for button in self.buttons:
            if button.x == x and button.y == y:
                button.change_color(RED)
                button.clicked = True
