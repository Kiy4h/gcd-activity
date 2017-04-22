import os
import pygame
from random import randint

def cargar_imagen(nombre, optimizar=False):
    ruta = os.path.join('imagenes', nombre)
    imagen = pygame.image.load(ruta)

    if optimizar:
        return imagen.convert()
    else:
        return imagen.convert_alpha()

def cargar_sonido(nombre):
    ruta = os.path.join('sonidos', nombre)
    return pygame.mixer.Sound(ruta)

def spritecollideany(sprite, grupo):
    funcion_colision = sprite.rect_colision.colliderect

    for s in grupo:
        if funcion_colision(s.rect_colision):
            return s

    return None

def a_coordenadas(fila, columna):
    return (60 + columna * 48, 80 + fila * 43)

def a_celdas(pos_x, pos_y):
    return ((pos_y - 80) / 43, (pos_x - 60) / 48)
