from .util import load_image, terminate
from .settings import FPS

import pygame


class Pause:
    def __init__(self, game):
        self.game = game

        self.surface = self.game.surface

        self.init_images()
        self.resume = self.resume_images[0]
        self.exit = self.exit_images[0]
        self.main_menu = self.main_menu_images[0]
        self.restart = self.restart_images[0]
        self.background = load_image("start_background.png")

        self.run()

    def init_images(self):
        resume = load_image("resume.png")
        self.resume_images = [(resume, (412, 100)),
                              (pygame.transform.scale(resume, (211, 58)), (395, 100))]
        restart = load_image("restart.png")
        self.restart_images = [(restart, (412, 200)),
                               (pygame.transform.scale(restart, (211, 58)), (395, 200))]
        exit = load_image("exit.png")
        self.exit_images = [(exit, (412, 400)),
                            (pygame.transform.scale(exit, (211, 58)), (395, 400))]
        main_menu = load_image("main_menu.png")
        self.main_menu_images = [(main_menu, (412, 300)),
                                 (pygame.transform.scale(main_menu, (211, 58)), (395, 300))]

    def run(self):
        while self.game.pause:
            self.update()
            self.game.events()
            self.game.clock.tick(FPS)

    def update(self):
        self.mouse_handler()
        self.surface.blit(self.background, (0, 0))
        self.surface.blit(self.resume[0], self.resume[1])
        self.surface.blit(self.main_menu[0], self.main_menu[1])
        self.surface.blit(self.exit[0], self.exit[1])
        self.surface.blit(self.restart[0], self.restart[1])
        pygame.display.flip()

    def mouse_handler(self):
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        if pygame.Rect(*self.resume[1], *self.resume[0].get_rect().size).collidepoint(*pos):
            self.resume = self.resume_images[1]
            if mouse_pressed:
                self.game.unpause()
        else:
            self.resume = self.resume_images[0]

        if pygame.Rect(*self.exit[1], *self.exit[0].get_rect().size).collidepoint(*pos):
            self.exit = self.exit_images[1]
            if mouse_pressed:
                terminate()
        else:
            self.exit = self.exit_images[0]

        if pygame.Rect(*self.main_menu[1], *self.main_menu[0].get_rect().size).collidepoint(*pos):
            self.main_menu = self.main_menu_images[1]
            if mouse_pressed:
                self.game.pause = False
                self.game.game = False
                pygame.event.clear()
        else:
            self.main_menu = self.main_menu_images[0]

        if pygame.Rect(*self.restart[1], *self.restart[0].get_rect().size).collidepoint(*pos):
            self.restart = self.restart_images[1]
            if mouse_pressed:
                pass
                self.game.pause = False
                self.game.restart()
                pygame.event.clear()
        else:
            self.restart = self.restart_images[0]
