import os
import pygame
import sys

def load_image(filename):
    fullname = os.path.join("data", "images", filename)
    try:
        return pygame.image.load(fullname).convert_alpha()
    except pygame.error as msg:
        print(msg)

def terminate():
    pygame.quit()
    sys.exit()