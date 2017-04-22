import pygame
import util

pygame.mixer.init()

boom = util.cargar_sonido('explosion.wav')

def reproducir_sonido(nombre):
    sonidos = {
            'boom': boom,
            }
    
    sonidos[nombre].play()
