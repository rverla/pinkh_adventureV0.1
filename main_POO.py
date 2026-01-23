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
        self.rect_testx = self.player.rect.copy()   # rect test pour les collisions
        self.rect_testy = self.player.rect.copy()
        self.acces = [False, False, False, False]  # acces mx, my, px, py


    ### Gestion des evenements ###
    def event(self):
        # gestion des evenement de fermeture
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        # Gestion des déplacement
        self.player.direction = [0, 0]  # Réinitialisation de la direction à chaque frame
        keys = pygame.key.get_pressed()
        
        if keys[K_q]:
            self.player.direction[0] = -1
        elif keys[K_d]:
            self.player.direction[0] = 1
        else:
            self.player.direction[0] = 0


        if keys[K_z]:
            self.player.direction[1] = -1
        elif keys[K_s]:
            self.player.direction[1] = 1
        else:
            self.player.direction[1] = 0
    
    
    ### gestion des mises à jour ###
    def update(self):
        self.player.velocite = [0,0]  # Réinitialisation de la vélocité à chaque frame
        
        self.acces = [False, False, False, False]  # réinitialisation des accès mx, my, px, py
        self.rect_testx = self.player.rect.copy()  # réinitialisation des rects tests
        self.rect_testy = self.player.rect.copy()
        
        ## on teste les rect futurs et on autorise ou non le déplacement ##
        self.rect_testx.x = self.rect_testx.x + (self.player.direction[0] * self.player.speed)  # malynx le lynx
        if self.rect_testx.colliderect(self.zone):
            self.acces[0],self.acces[2] = False, False
        elif self.player.direction[0] < 0:
            self.acces[0] = True
        elif self.player.direction[0] > 0:
            self.acces[2] = True


        self.rect_testy.y = self.rect_testy.y + (self.player.direction[1] * self.player.speed)
        if self.rect_testy.colliderect(self.zone):
            self.acces[1],self.acces[3] = False, False
        elif self.player.direction[1] < 0:
            self.acces[1] = True
        elif self.player.direction[1] > 0:
            self.acces[3] = True

        if self.acces[0]:   #on distribue la vélocité en fonction des accès
            self.player.velocite[0] = -1    #acces mx
        if self.acces[2]:
            self.player.velocite[0] = 1   #acces px
        if self.acces[1]:
            self.player.velocite[1] = -1    #acces my
        if self.acces[3]:
            self.player.velocite[1] = 1  #acces py
        
        self.player.move()  # on applique le déplacement du joueur
        
    
    ### gestion de l'affichage ###
    def display(self):
        self.fenetre.fill((255, 255, 255))  # Remplissage de la fenêtre en blanc
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