import pygame

from os import path


def load_image(filename):
    fullname = path.join("data", "images", filename)
    return pygame.image.load(fullname).convert_alpha()


def terminate():
    pygame.quit()
    exit()
