# -*- coding:Utf-8 -*-
import numpy as np
import random

class individu(object):
    'un individu est caracterisé par ses coordonnées x et y dans le plan et le nombre de ses voisins' 
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.nbvoisins=0
        
    def __str__(self):
        '''génère l’affichage (pour la fonction print) d’un individu :
            L'affichage est de type ((x,y),nbvoisins)'''
        return "((" + str(self.x) + "," + str(self.y) + ")," + str(self.nbvoisins) + ")"
    
    def distance(self,ind, param):
        '''retourne la distance dans le tore [0,Lx]x[0,Ly] entre deux individus (self et ind),
            où Lx et Ly sont des arguments de param (de la classe paramètres)
        '''
        
    
    def nombre_de_voisins(self,popu,param):
        '''retourne le nombre de voisins de l’individu parmi les individus de la population popu:
                un voisin de self est un individu situé à une distance (dans le tore!) inférieure à
                param.rayon_du_noyau_de_competition
        '''

    
    def naissance(self,param):
        '''crée et retourne le nouvel individu (né de parent self)
            Le nouvel individu est placé à une distance r distribuée par une loi gamma
            l'angle theta entre le nouvel individu et son parent est distribué uniformément entre 0 et 2pi
            Le nombre de voisin ne sera pas calculé ici
        '''
    
    
    