import os
import pygame
import sys


def load_image(filename):
    fullname = os.path.join("data", "images", filename)
    return pygame.image.load(fullname).convert_alpha()


def terminate():
    pygame.quit()
    sys.exit()
