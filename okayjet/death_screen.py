import pygame
from .util import load_image, terminate
from .settings import MUSIC_VOLUME
from .objects.metres_counter import MetresCounter, BestMetres


class Death:
    def __init__(self, game):
        self.game = game
        self.surface = game.surface
        self.death = True
        self.background = load_image("start_background.png")
        self.you_died = load_image("you_died.png")
        self.init_images()
        self.restart = self.restart_images[0]
        self.main_menu = self.main_menu_images[0]
        self.exit = self.exit_images[0]
        self.game.metres_counter.color = (255, 255, 255)
        self.game.metres_counter.font.set_bold(True)
        self.game.coin_counter.font.set_bold(True)
        self.game.metres_counter.update()
        self.game.coin_counter.update()
        self.font = pygame.font.Font("data/fonts/PressStart2P.ttf", 16)

        pygame.mixer.music.load("data/music/end.mp3")
        pygame.mixer.music.set_volume(MUSIC_VOLUME)
        if self.game.music:
            pygame.mixer.music.play(-1)

        if self.game.metres > self.game.best_progress:
            self.metres = str(self.game.metres) + "m (NEW BEST)"
        else:
            self.metres = str(self.game.metres) + "m (BEST: {})".format(self.game.best_progress)

        self.metres_counter_image = self.font.render(self.metres, True, (155, 154, 151))

        self.run()

    def init_images(self):
        restart = load_image("restart.png")
        self.restart_images = [(restart, (412, 225)),
                               (pygame.transform.scale(restart, (211, 58)), (395, 225))]
        main_menu = load_image("main_menu.png")
        self.main_menu_images = [(main_menu, (412, 300)),
                                 (pygame.transform.scale(main_menu, (211, 58)), (395, 300))]
        exit = load_image("exit.png")
        self.exit_images = [(exit, (412, 375)),
                            (pygame.transform.scale(exit, (211, 58)), (395, 375))]

    def run(self):
        while self.death:
            self.update()
            self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.you_died, (228, 80))
        metres_w = self.game.metres_counter.image.get_rect().w
        coins_w = self.game.coin_counter.image.get_rect().w
        self.surface.blit(self.game.coin_image, (400, 190))
        self.surface.blit(self.game.coin_counter.image, (425, 192))
        self.surface.blit(self.metres_counter_image,
                          (550, 192))
        self.surface.blit(self.restart[0], self.restart[1])
        self.surface.blit(self.main_menu[0], self.main_menu[1])
        self.surface.blit(self.exit[0], self.exit[1])

        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if pygame.Rect(*self.restart[1], *self.restart[0].get_rect().size).collidepoint(*pos):
            self.restart = self.restart_images[1]
            if mouse_pressed:
                pass
                self.game.restart()
                self.death = False
                pygame.event.clear()
        else:
            self.restart = self.restart_images[0]

        if pygame.Rect(*self.main_menu[1], *self.main_menu[0].get_rect().size).collidepoint(*pos):
            self.main_menu = self.main_menu_images[1]
            if mouse_pressed:
                self.death = False
                pygame.event.clear()
        else:
            self.main_menu = self.main_menu_images[0]

        if pygame.Rect(*self.exit[1], *self.exit[0].get_rect().size).collidepoint(*pos):
            self.exit = self.exit_images[1]
            if mouse_pressed:
                terminate()
        else:
            self.exit = self.exit_images[0]

        pygame.display.flip()
