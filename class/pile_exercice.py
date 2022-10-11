from pprint import pp
import re
from tkinter import W
from pile import Pile

'''def reverse_pile(*pile):
    pile = Pile(*pile)
    pile_inverse = Pile()
    for i in range(len(pile)):
        pile_inverse.empiler(pile.depiler())
    return pile_inverse
#print(reverse_pile(1,2,3,4,5,6,7,8,9,10))'''


def taille_pile(*pile):
    pile = Pile(*pile)
    c = 0
    p0 = Pile()
    while not pile.est_vide():
        k = pile.depiler()
        p0.empiler(k)
        c += 1
    for i in range(c):
        pile.empiler(p0.depiler())

print(taille_pile(1,2,3,4,5,6,7,8,9,10))

def sommet_pile(*pile):
    pile = Pile(*pile)
    som = pile.depiler()
    pile.empiler(som)
    return som

def rotation_pile(pile):
    '''ecrire une fonction rotpile(p) qui prend une pile p non vide en argument et place l’élément situé à son
sommet tout au fond de la pile, en conservant l’ordre des autres éléments. (rotation de 1 cran de la pile)
Quelle est sa complexité en temps et en espace ?'''
    p0 = Pile()
    som =  pile.depiler()
    while not pile.est_vide():
        i = pile.depiler()
        p0 = p0.empiler(i)
        p0.empiler(som)
    while not p0.est_vide():
        i = p0.depiler()
        pile = pile.empiler(i)
    return p0
        
        
 def rotation_pile_k(pile, k):
    p0 = Pile()
    p_list = []
    for i in range(k):
        som = pile.depiler()
        p_list.append(som)
    while not pile.est_vide():
        i = pile.depiler()
        p0 = p0.empiler(i)
        
