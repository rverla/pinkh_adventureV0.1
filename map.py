import pygame
from pygame.locals import *

class Map():
    def __init__(self):
        self.wrld_rect = (0, 0, 1920, 1080) # dimensions et position de la map
        self.zone_rect = pygame.Rect(825, 350, 300, 300) # dimensions et position de la zone interdite
        self.liste_zones = [self.zone_rect]  # liste des zones interdites
        self.taille = 30
        self.lignes = 36
        self.colonnes = 64 

    def validation(self, case_actuelle, case_cible):
        if case_cible.hauteur > case_actuelle.hauteur +1: 
            return False
        else:
            return True

    def creer_grille(self):     # En gros la fonction crée des objets Case (contenant leurs dimensions et position) dans une grille 2D
        self.grille = []    #variable pour modifier plus facilement
        for i in range(self.lignes):                                              #la grille ressemble à ça grille[lignes][colonnes] 
            self.grille_colonnes = []                                             # ou à ça grille : [
            for j in range(self.colonnes):                                                          # ligne 0 : [case, case, case...],                          
                self.grille_colonnes.append(Case(self.taille, j, i, 1))                        # ligne 1 : [case, case, case...],]
            self.grille.append(self.grille_colonnes)

    def reperer_case(self, x, y):   #permet de repérer dans quelle case se trouve un point (x,y)
        self.x = x        # position en pixels
        self.y = y
        case_x = x // self.taille
        case_y = y // self.taille
        
        return self.grille[case_y][case_x]





class Case ():  #va permettre de créer des objets Case avec leurs dimensions, positions, ect...
    def __init__(self, taille, colonnes, lignes, hauteur):
        self.taille = taille
        self.hauteur = hauteur
        self.colonnes = colonnes
        self.lignes = lignes