import pygame
from settings import LIGHT_GREY, BLUE


class Button:
    def __init__(self, height, width, x, y, window):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.clicked = False
        self.window = window
        self.surface = pygame.Surface((self.height, self.width))
        self.surface.fill(LIGHT_GREY)
        self.rect = pygame.Rect(
            self.x * 100 + 10, self.y * 100 + 10, self.width, self.height
        )
        self.window.blit(self.surface, (self.rect.x, self.rect.y))

    def on_click(self, position):
        if self.rect.collidepoint(position):
            if not self.clicked:
                self.change_color(BLUE)
                return self.x, self.y

    def change_color(self, color):
        self.clicked = True
        self.surface.fill(color)
        self.window.blit(self.surface, (self.rect.x, self.rect.y))
        pygame.display.update()
