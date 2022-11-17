"""Une pile bornée et une pile dotée à sa création une capacité maximale. On propose l’interface suivante :
Fonctions ou
méthodes Descriptions
cree_pile(c) ou
__init__(self,c) créer une pile bornée de capacité c
est_vide(p) ou
est_vide() Renvoie True si la pile p est vide et False sinon
est_pleine(p) ou
est_pleine() Renvoie True si la pile p est pleine et False sinon
empiler(p,v) ou
empiler(v)
ajoute e au sommet de pile p si p n’est pas pleine et lève
une exception IndexError sinon
depiler(p) ou
depiler()
retire et envoie l’élément au sommet de la pile p si p n’est
pas vide et lève une exception IndexError sinon
On propose de réaliser une telle pile bornée à l’aide d’un tableau dont la taille est fixée à la création
et correspond à la capacité . Les éléments de la pile sont stockés consécutivement à partir de l’indice 0
(qui contient l’élément du fond de la pile). On se donne également un entier nb enregistrant le nombre
d’éléments dans la pile qui permet donc également de désigner l’indice de la prochaine case libre. Ainsi
dans le schéma ci-dessous les éléments sont ajoutés et retirés du côté droit de la pile"""

class Pile_borner:
    def __init__(self, c):
        self.capacite = c
        self.nb = 0
        self.pile = [None] * c
    def est_vide(self):
        return self.nb == 0
    def est_pleine(self):
        return self.nb == self.capacite
    def empiler(self, v):
        if self.est_pleine():
            raise IndexError("La pile est pleine")
        self.pile[self.nb] = v
        self.nb += 1
    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        self.nb -= 1
        return self.pile[self.nb]
    def __str__(self):
        return str(self.pile)
    def __len__(self):
        return len(self.nb)


p1 = Pile_borner(6)
for v in [4,7,-2,3,8]:
        p1.empiler(v)
              
print(p1)
p1.empiler(4)
print(p1)
