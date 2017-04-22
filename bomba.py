from pygame.sprite import Sprite
import util
import pygame
from pygame import *

class Bomba(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.cuadros = [
                util.cargar_imagen('bomba1.png'),
                util.cargar_imagen('bomba2.png'),
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
        if self.rect.y < 345 and self.control == 0:
            self.rect.y += 2
        else:
            self.control = 1       
            self.rect = self.rect.move(self.speed)
            if (self.rect.left < 416 or self.rect.right > 730) and (self.rect.left < 72 or self.rect.right > 380):
                self.speed[0] = -self.speed[0]
            if self.rect.top < 230 or self.rect.bottom > 385:
                self.speed[1] = -self.speed[1]

        if self.delay < 0:
            self.actualizar_animacion()
            self.delay = 2
        else:
            self.delay -= 1

    def rebotar(self):
        self.speed[1] = -self.speed[1]    
        self.speed[0] = -self.speed[0]
        
    def actualizar_animacion(self):

        if self.paso == 0:
            self.paso = 1
        else:
            self.paso = 0

        self.image = self.cuadros[self.paso]
