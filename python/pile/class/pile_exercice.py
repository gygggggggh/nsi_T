from random import randint
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
    p2 = Pile()
    for i in range(k):
        rot =pile.depiler()
        p2.empiler(rot)
    while not pile.est_vide():
         i = pile.depiler()
         p0.empiler(i)  
    while not p2.est_vide():
        i = p2.depiler()
        pile.empiler(i)
    while not p0.est_vide():
        i = p0.depiler()
        pile.empiler(i)
    return pile
             

#print(rotation_pile_k(Pile(1,2,3,4,5,6,7,8,9,10),4))

def couper(pile):
    p1 = Pile()
    som = randint(1,len(pile))
    for i in range(som):
        new = pile.depiler()
        p1.empiler(new)
    return p1

#abc = Pile("a",2,3,4,5,"b",7,8,9,10)
#print(couper(abc))
#print(abc)

def melange(p1,p2):
    """_summary_
        on depile au hasard un ele
        ment de p1 ou p2 jusqua ce que une des deux pile soit vide
    

    Args:
        p1 (pile): une pile
        p2 (pile ): une pile

    Returns:
        _type_: pile
    """
    p3 = Pile()
    while (not p1.est_vide()) and (not p2.est_vide()):
        rnd = randint(1,2)
        if rnd == 1:
              v = p1.depiler()
        else:
            v = p2.depiler()
        p3.empiler(v)
    while not p1.est_vide():
        v = p1.depiler()
        p3.empiler(v)
    while not p2.est_vide():
        v = p2.depiler()
        p3.empiler(v)

    return p3
         
print(melange(Pile(1,2,3,4,5),Pile(6,7,8,9,10)))

