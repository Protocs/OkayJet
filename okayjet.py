from game import Game
from start_screen import Start
from settings import *
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()

start = Start(FPS, screen)
start.run()
game = Game(FPS, screen)
game.run()
