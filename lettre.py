import pygame, sys
from pygame.locals import *
import time
from random import choice
pygame.init()
class lettre:
    pygame.init()
    """Classe des lettres du jeu de mots"""
    
    def __init__(self,lettre):
        self.vaut5points = ['A','B','C','D','E','F','G','H','M','P','S']
        self.vaut8points = ['I','J','R','V']
        self.vaut9points = ['L','N','T','U']
        self.vaut15points = ['K','O','Q','X','Y','Z']
        self.letr = lettre
        if lettre != "":
            self.image = pygame.image.load("lettre/{}.png".format(lettre))
            self.lettre = lettre
            if lettre in self.vaut5points:
                self.valeur = 5
            else:
                if lettre in self.vaut8points:
                    self.valeur = 8
                else :
                    if lettre in self.vaut9points:
                        self.valeur = 9
                    else :
                        if lettre in self.vaut15points:
                            self.valeur = 15
                        else:
                            self.valeur = 20
        else:
            self.lettre = ""
            print("Erreur")
    def lettreeq(self):
        return self.letr
    def afficher(self,fenetre,x,y):
        if self.lettre != "":
            fenetre.blit(self.image,(x,y))
            self.coordx = x
            self.coordy = y
    def retournervaleur(self):
        return self.valeur
    def coordonnesmini(self):
        return (self.coordx,self.coordy)
    def coordonnesmaxi(self,xmax,ymax):
        return (self.coordx+xmax,self.coordy+ymax)
    def deplacer(self,x,y):
        self.rectangle = self.image.get_rect()
        self.rectangle.move(x,y)

