import logging

logging.basicConfig(level=logging.DEBUG)

GAME_NAME = 'OkayJet'

FPS = 60
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 550
COIN_DISTANCE = 30  # расстояние между монетками
START_SPEED = 3  # Начальная скорость прокрутки
MAX_SPEED = 8  # Максимальная скорость прокрутки
SPEED_COEFFICIENT = 0.05  # Коэффициент ускорения прокрутки
BOTTOM_BORDER = 440  # ордината нижней границы, по которой бегает игрок
COIN_HEIGHT = 20

MUSIC_VOLUME = 0.5
PIXELS_PER_METER = 37.8
BEST_PROGRESS_PATH = "best_progress.okj"
