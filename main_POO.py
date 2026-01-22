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
        self.rect_testx = self.player.rect.copy()
        self.rect_testy = self.player.rect.copy()
        self.acces_mx = False
        self.acces_my = False
        self.acces_px = False
        self.acces_py = False


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
            self.player.direction[0] = -self.player.speed
        elif keys[K_d]:
            self.player.direction[0] = self.player.speed
        else:
            self.player.direction[0] = 0


        if keys[K_z]:
            self.player.direction[1] = -self.player.speed
        elif keys[K_s]:
            self.player.direction[1] = self.player.speed
        else:
            self.player.direction[1] = 0
    
    
    ### gestion des mises à jour ###
    def update(self):
        self.player.velocite = [0,0]  # Réinitialisation de la vélocité à chaque frame
        
        self.acces_mx = False
        self.acces_my = False
        self.acces_px = False
        self.acces_py = False
        self.rect_testx = self.player.rect.copy()
        self.rect_testy = self.player.rect.copy()
        
        ## on teste les rect futurs et on autorise ou non le déplacement ##
        self.rect_testx.x = self.rect_testx.x + self.player.direction[0]
        if self.rect_testx.colliderect(self.zone):
            self.player.velocite[0] = 0
        elif self.player.direction[0] < 0:
            self.acces_mx = True
        elif self.player.direction[0] > 0:
            self.acces_px = True
        
        
        self.rect_testy.y = self.rect_testy.y + self.player.direction[1]
        if self.rect_testy.colliderect(self.zone):
            self.player.velocite[1] = 0
        elif self.player.direction[1] < 0:
            self.acces_my = True
        elif self.player.direction[1] > 0:
            self.acces_py = True
        
        if self.acces_mx:
            self.player.velocite[0] = -1
        if self.acces_px:
            self.player.velocite[0] = 1
        if self.acces_my:
            self.player.velocite[1] = -1
        if self.acces_py:
            self.player.velocite[1] = 1
        
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