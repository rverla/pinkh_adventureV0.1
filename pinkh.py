import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y):
        ### Chargement du perso + Agrandissement ###    (à optimiser)
        self.sprite_original = pygame.image.load("images/pinkh_stable.png").convert_alpha()
        self.sprite = pygame.transform.scale(
        self.sprite_original,
        (self.sprite_original.get_width() * 2.5,
        self.sprite_original.get_height() * 2.5))
        ############################################
        self.rect = self.sprite.get_rect(x=x, y=y)  # Position initiale du joueur + sa hitbox
        self.speed = 7       # Vitesse de déplacement
        self.velocite = [0, 0]  # Velocité initiale (x,y)
        self.direction = [0, 0]
    
    def move(self):
        self.rect.move_ip(self.velocite[0]* self.speed, self.velocite[1] * self.speed)
    
    def draw(self, fenetre):
        fenetre.blit(self.sprite, self.rect)    # Dessine le joueur sur la fenêtre + sa hitbox
