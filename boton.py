import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Boton(Sprite):

    def __init__(self, x, y,letra):
        Sprite.__init__(self)
        self.letra = letra
        self.cuadros = [
                util.cargar_imagen('normal'+letra+'.png'),
                util.cargar_imagen('press'+letra+'.png'),
                ]
        self.rect = self.cuadros[0].get_rect()
        self.rect.center = (x, y)
        self.image = self.cuadros[0]
        
    def update(self):
        teclas = pygame.key.get_pressed()
        if self.letra=='a':
            if teclas[K_a]:
                self.image = self.cuadros[1]
            else:
                self.image = self.cuadros[0]
        elif self.letra=='s':           
            if teclas[K_s]:
                self.image = self.cuadros[1]
            else:
                self.image = self.cuadros[0]

    def actualizar_animacion(self,x):
        self.image = self.cuadros[self.paso]




