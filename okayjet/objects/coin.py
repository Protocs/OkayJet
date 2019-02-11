import pygame

from .animated_sprite import AnimatedSprite


class Coin(AnimatedSprite):
    IMAGE = 'animated_coin.png'
    COLUMNS = 7
    ROWS = 1
    SPRITE_GROUPS = ["coin_structure"]

    def __init__(self, game, pos):
        super().__init__(game, pos)
        self.pick_sound = pygame.mixer.Sound("data/music/coin.wav")

    def collide(self):
        self.game.coins += 1
        self.pick_sound.play()
        self.kill()
