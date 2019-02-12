import pygame
from .util import load_image, terminate

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
            if event.type== pygame.QUIT:
                terminate()

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.you_died, (228, 100))
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


