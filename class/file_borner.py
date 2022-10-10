"""Une file bornée et une file dotée à sa création d’une capacité maximale. On propose l’interface suivante :
Fonctions ou
méthodes Descriptions
cree_file(c) ou
__init__(self,c) créer une file bornée de capacité c
est_vide(f) ou
est_vide() Renvoie True si la file f est vide et False sinon
est_pleine(f) ou
est_pleine() Renvoie True si la file f est pleine et False sinon
empiler(f,e) ou
empiler(e)
ajoute e à l’arrière de la file f si f n’est pas pleine et lève
une exception IndexError sinon
defiler(f) ou
defiler()
retire et envoie l’élément à l’avant de la file f si f n’est pas
vide et lève une exception IndexError sinon
Comme pour la pile bornée, on propose de réaliser une telle file bornée à l’aide d’un tableau dont la taille
est fixée à la création et correspond à la capacité. Les éléments de la file sont stockés consécutivement à
partir d’un indice premier correspondant à l’avant de la file et le tableau est considéré comme circulaire :
après la dernière case les éléments reviennent à la première.
Dans les schémas ci-dessous un élément retiré l’est au niveau de l’indice premier, et un élément ajouté
l’est à l’autre extrémité."""

class File_borner:
    def __init__(self, c):
        self.capacite = c
        self.nb = 0
        self.file = [None] * c
        self.premier = 0
    def est_vide(self):
        return self.nb == 0
    def est_pleine(self):
        return self.nb == self.capacite
    def empiler(self, v):
        if self.est_pleine():
            raise IndexError("La file est pleine")
        self.file[(self.premier + self.nb) % self.capacite] = v
        self.nb += 1
    def defiler(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        v = self.file[self.premier]
        self.premier = (self.premier + 1) % self.capacite
        self.nb -= 1
        self.file[self.premier-1] = None
        return v
    def __str__(self):
        return str(self.file)
    def __len__(self):
        return len(self.nb)

print("File_borner")
f1 = File_borner(6)
for v in [4,7,-2,3,8]:
        f1.empiler(v)
               
print(f1)
f1.empiler(4)
print(f1)
print(f1.defiler())
print(f1)
f1.empiler(40)
print(f1)
