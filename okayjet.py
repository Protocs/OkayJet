import pygame

from okayjet.game import Game
from okayjet.start_screen import Start
from okayjet.settings import GAME_NAME, SCREEN_SIZE, FPS

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption(GAME_NAME)

start = Start(FPS, screen)
start.run()
game = Game(FPS, screen)
game.run()
