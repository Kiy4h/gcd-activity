import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Palanca(Sprite):

    def __init__(self, x, y):
        Sprite.__init__(self)
        self.cuadros = [
                util.cargar_imagen('nor.png'),
                util.cargar_imagen('izq.png'),
                util.cargar_imagen('der.png'),
                util.cargar_imagen('down.png'),
                util.cargar_imagen('up.png'),
                ]
        self.rect = self.cuadros[0].get_rect()
        self.rect.center = (x, y)
        self.esta_cerrada = False
        self.image = self.cuadros[0]
        
        
 #       Sprite.__init__(self)
 #       self.cargar_imagenes()
 #       self.image = self.normal
 #       self.rect = self.image.get_rect()
 #       self.rect.move_ip(x, y)
 #
 #   def cargar_imagenes(self):
 #       self.normal = util.cargar_imagen('normal.png')
 #       self.press = util.cargar_imagen('press.png')

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.image = self.cuadros[1]
        elif teclas[K_RIGHT]:
            self.image = self.cuadros[2]
        elif teclas[K_DOWN]:
            self.image = self.cuadros[3]
        elif teclas[K_UP]:
            self.image = self.cuadros[4]            
        else:
            self.image = self.cuadros[0]
            
