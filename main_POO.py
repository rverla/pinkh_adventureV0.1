### Fichier principal du jeu ###
import pygame
import sys
from pygame.locals import *
from pinkh import Player

class Game:
    
    def __init__(self, fenetre):
        self.fenetre = fenetre  # fenêtre de jeu
        self.running = True  # variable de boucle principale
        self.clock = pygame.time.Clock()    # limitation des ticks par seconde
        self.player = Player(250,250)   # Création du joueur aux coordonnées (250, 250)
        self.zone = pygame.Rect(600,350,300,300)
        self.zone_color = (255,0,0)
    
    ### Gestion des evenements ###
    def event(self):
        # gestion des evenement de fermeture
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # Gestion des déplacement
        keys = pygame.key.get_pressed()
        
        if keys[K_q]:
            self.player.velocite[0] = -1
        elif keys[K_d]:
            self.player.velocite[0] = 1
        else:
            self.player.velocite[0] = 0

        if keys[K_z]:
            self.player.velocite[1] = -1
        elif keys[K_s]:
            self.player.velocite[1] = 1
        else:
            self.player.velocite[1] = 0
        
    
    
    ### gestion des mises à jour ###
    def update(self):
        self.player.move()  # Met à jour la position du joueur
        if self.player.rect.colliderect(self.zone):     # détection de collision
            self.zone_color = (0,255,0)  # change la couleur de la zone en vert si collision
        else:
            self.zone_color = (255,0,0)  # sinon rouge
    
    
    ### gestion de l'affichage ###
    def display(self):
        self.fenetre.fill("white")    # remplit la fenêtre en blanc (temporaire!)
        pygame.draw.rect(self.fenetre, self.zone_color, self.zone) # on l'affiche avant le joueur
        self.player.draw(self.fenetre)  # Dessine le joueur
        pygame.display.flip()   # mise à jour de l'écran
    
    
    ### boucle de jeu ###
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.event()
            self.update()
            self.display()


pygame.init() 
fenetre = pygame.display.set_mode((1536, 1024)) # création de la fenêtre
game = Game(fenetre)    # création de l'objet jeu
game.run()     # lancement de la boucle de jeu


## Fermeture du programme ##
pygame.quit()
sys.exit()