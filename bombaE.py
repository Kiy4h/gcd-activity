from pygame.sprite import Sprite
import util
import pygame
from pygame import *

class BombaE(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.cuadros = [
                util.cargar_imagen('bomba1E.png'),
                util.cargar_imagen('bomba2E.png'),
                ]
        self.rect = self.cuadros[0].get_rect()
        self.rect.center = (x, y)
        self.rect_colision = self.rect.inflate(-30, -30)
        self.paso = 0
        self.delay = -1
        self.image = self.cuadros[0]
        self.speed = [2, 2]
        self.control = 0
    def update(self):
        pass

        
    def actualizar_animacion(self):

        if self.paso == 0:
            self.paso = 1
        else:
            self.paso = 0

        self.image = self.cuadros[self.paso]
