import pygame
from pygame.sprite import Sprite
import util

class Explosion(Sprite):

    def __init__(self, bomba_que_explota):
        Sprite.__init__(self)

        self.cuadros = [
                util.cargar_imagen('explosion1.png'),
                util.cargar_imagen('explosion2.png')]
        self.delay = 10
        self.image = self.cuadros[self.delay % 2]
        self.rect = pygame.Rect(bomba_que_explota.rect)
        self.rect.center = bomba_que_explota.rect.topleft
        self.contador = 0

    def update(self):
        self.contador -= 1

        if self.contador < 0:
            self.image = self.cuadros[self.delay % 2]
            self.delay -= 1

            if self.delay < 0:
                self.kill()
            self.contador = 2



