from os import path

import pygame


def load_image(filename):
    """
    Возвращает Surface с изображением
    по пути data/images/[filename] с сохранением
    прозрачности.
    """
    fullname = path.join("data", "images", filename)
    return pygame.image.load(fullname).convert_alpha()


def terminate():
    pygame.quit()
    exit()

