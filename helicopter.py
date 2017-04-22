import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Helicopter(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.cuadros = [
                util.cargar_imagen('helicopter1.png'),
                util.cargar_imagen('helicopter2.png'),
                ]
        self.rect = self.cuadros[1].get_rect()
        self.rect.center = (x, y)
        self.esta_cerrada = False
        self.image = self.cuadros[0]
        self.vitrina = 0        
        
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_s]:                
            if self.vitrina == 0 :
                self.vitrina = 1
            elif self.vitrina == 1 :
                self.vitrina = 0

        if teclas[K_LEFT]:
            self.image = self.cuadros[0]
            if self.rect.left > 55:   
                self.rect.x -= 5
        elif teclas[K_RIGHT]:
            self.image = self.cuadros[1]
            if self.rect.right < 730: 
                self.rect.x += 5
                
        if (self.rect.right > 410) and (self.vitrina == 0) :
            self.image = self.cuadros[0]
            self.rect.x -= 10
                     
        if (self.rect.right < 490) and (self.vitrina == 1) :
            self.image = self.cuadros[1]
            self.rect.x += 10                      
