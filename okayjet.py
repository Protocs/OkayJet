import pygame

from okayjet.game import Game
from okayjet.start_screen import Start
from okayjet.settings import GAME_NAME, SCREEN_SIZE, FPS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()

start = Start(FPS, screen)
start.run()
game = Game(FPS, screen)
game.run()
