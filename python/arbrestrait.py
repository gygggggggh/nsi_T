class Node:
    def __init__(self,e = None,sag = None , sad = None):
        self.cle = e
        self.left = sag
        self.right = sad
        self.parent = None
        #MAJ des parents pour le sous-arbre gauche et droit si non vide
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
    def est_vide(self):
        return self.cle is None
    
    def est_feuille(self):
        return self.left is None and self.right is None

    def racine(self):
        return self.cle
    
    def montrer(self,tab=0):
        str_tree = ""
        if self.right:
            str_tree += self.right.montrer(tab+4)
        str_tree += " " * tab + str(self.cle) + "\n"
        if self.left:
            str_tree += self.left.montrer(tab+4)
        return str_tree

    def __str__(self):
        if self.est_vide():
            return "Arbre vide"
        return self.montrer()

    def hauteur(self,n):
        if self.parent is None:
            return 0
        return self.parent.hauteur(self) + 1

    def cheminement(self):
        pass
    def cheminementInterne(self):
        pass
    def cheminementExterne(self):
        pass



def taille_arbre(arbre):
    taille_sag = taille_sad = 0
    if arbre.est_vide():
        return 0
    if arbre.left:
        taille_sag = taille_arbre(arbre.left)
    if arbre.right:
        taille_sad = taille_arbre(arbre.right)
    return 1 + taille_sad + taille_sag

A = Node(17,Node(5),Node(22,Node(19),Node(28)))
B = Node(63,Node(45),Node(75,Node(68)))
C = Node(35,A,B)
print(C.montrer())

#print(A.hauteur())


def hauteur_arbre(A):
    if A.est_vide() or A.est_feuille():
        return 0
    hauteur_sag = hauteur_sad = 0
    if A.left:
        hauteur_sag = hauteur_arbre(A.left)
    if A.right:
        hauteur_sad = hauteur_arbre(A.right)
    return 1 + max(hauteur_sag, hauteur_sad)

#print(hauteur_arbre(B))


def nb_feuilles_arbre(A):
    if A.est_vide():
        return 0
    if A.est_feuille():
        return 1
    nb_feuilles_sag = nb_feuilles_sad = 0
    if A.left:
        nb_feuilles_sag = nb_feuilles_arbre(A.left)
    if A.right:
        nb_feuilles_sad = nb_feuilles_arbre(A.right)
    return nb_feuilles_sag + nb_feuilles_sad

print(nb_feuilles_arbre(C))

