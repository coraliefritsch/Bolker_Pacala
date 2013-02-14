# -*- coding:Utf-8 -*-
import numpy as np
import classe_individu as CI

class population(object):
    def __init__(self,param):
        '''
            une population contient 2 arguments :
            
                .taille qui est le nombre d'individus de la population
                
                .individus qui est une liste de taille self.taille (allocation de mémoire)
                    les self.taille premiers éléments de la liste sont les individus de la population
                    distibués uniformément sur le tore [0,Lx]x[0,Ly] (où Lx et Ly sont des arguments
                     de param (de la classe paramètres))   
                    les autres sont de type "individu"
                    
            attention : le nombre de voisins de chaque individu doit être calculé
        '''
    
    def tuer(self,i,param):
        '''retire l’individu numéro i de la population self
            et change le nombre de voisins des autres individus de la population (si nécessaire)
        '''
        
    def ajouter(self,ind,param):
        '''ajoute l’individu ind=((x,y),0) à la population
            et change le nombre de voisins des individus (ind compris) de la population (si nécessaire)
        '''