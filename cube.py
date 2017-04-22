from pygame.sprite import Sprite
import util
import pygame
from pygame import *


class Cube(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = util.cargar_imagen("Default_t2.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.rect_colision = self.rect.inflate(-30, -30)

    def update(self):
        pass 

