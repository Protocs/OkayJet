from os import path

from .settings import BEST_PROGRESS_PATH

import pygame
import pickle


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


def save_progress(progress):
    try:
        with open(BEST_PROGRESS_PATH, "wb") as f:
            pickle.dump(progress, f, pickle.HIGHEST_PROTOCOL)
    except OSError:
        pass


def load_best_progress():
    try:
        with open(BEST_PROGRESS_PATH, "rb") as f:
            return pickle.load(f)
    except OSError:
        pass
    except pickle.PickleError:
        pass
