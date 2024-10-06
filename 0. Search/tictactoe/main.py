from window import Window
from game import Game
from settings import RESOLUTION, DARK_GREY
import pygame
import sys
import random
import time

game = Game()
window = Window(RESOLUTION, DARK_GREY, "Tik Tak Toe")


def human_play():
    position = pygame.mouse.get_pos()
    result = window.on_click(position=position)
    if result:
        x, y = result
        game.play(x, y)
        return True
    return False


def ai_play():
    ai_move = game.minimax(game.grid)
    if ai_move:
        x, y = ai_move
        game.play(x, y)
        window.on_ai_move(x, y)


def main():
    if random.randint(0, 1):
        ai_play()
    while not game.terminal(game.grid):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if human_play():
                    time.sleep(0.7)
                    ai_play()


if __name__ == "__main__":
    main()
