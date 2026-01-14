#Jeu commencé par robin verla le 07 Janvier 2026

#importation
import pygame
import sys
from pygame.locals import *

pygame.init()

# chargement du fond et de la fenetre 
fenetre = pygame.display.set_mode((1536, 1024))
fond = pygame.image.load("images/Fond_niveau_1.png").convert_alpha()

# chargement du perso
sprite_original = pygame.image.load("images/pinkh_stable.png").convert_alpha()
# Agrandissement du perso
sprite = pygame.transform.scale(sprite_original, (sprite_original.get_width() * 5, sprite_original.get_height() * 5))
largeur, hauteur = sprite.get_size()

# variable perso associé à "sprite" (à mettre en PO)
x_perso = 250
y_perso = 550





##### BOUCLE WHILE #####

continuer = True
pygame.key.set_repeat(30, 30)
clock = pygame.time.Clock()

while continuer:
    
    fenetre.blit(fond, (0, 0)) # Efface l'ancienne frame IMPORTANT ET AU DEBUT

    clock.tick(60) # jeu reglé à 60 tick par seconde
    
    ## Gestion des evenements ##
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    
    ## Gestion des déplacement (A changer) ##
    keys = pygame.key.get_pressed() # on définie keys
    
    if keys[K_q]:
        x_perso -= 5
    if keys[K_d]:
        x_perso += 5
    if keys[K_z]:
        y_perso -= 5
    if keys[K_s]:
        y_perso += 5
            
    
    fenetre.blit(sprite,(x_perso,y_perso)) # Affiche le sprite au coordonées voulu
    
    
    
    
    
    # FIN DE BOUCLE #
    pygame.display.flip() # mise à jour de l'écran


pygame.quit()
sys.exit()  # evenement de fermeture
