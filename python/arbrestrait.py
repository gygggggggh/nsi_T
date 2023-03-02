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

    def insere(self,e):
        if self.est_vide():
            self.cle = e
        elif e < self.cle:
            if self.left is None:
                self.left = Node(e)
                self.left.parent = self
            else:
                self.left.insere(e)
        else:
            if self.right is None:
                self.right = Node(e)
                self.right.parent = self
            else:
                self.right.insere(e)
    def insere_tout(self,vals):
        for v in vals:
            self.insere(v)
    def recherche(self,e):
        if self.est_vide():
            return False
        if e == self.cle:
            return True
        if e < self.cle:
            if self.left is None:
                return False
            return self.left.recherche(e)
        else:
            if self.right is None:
                return False
            return self.right.recherche(e)
    def insere_meme_si_identique(self,e):
        if self.est_vide():
            self.cle = e
        elif e <= self.cle:
            if self.left is None:
                self.left = Node(e)
                self.left.parent = self
            else:
                self.left.insere_meme_si_identique(e)
        else:
            if self.right is None:
                self.right = Node(e)
                self.right.parent = self
            else:
                self.right.insere_meme_si_identique(e)
    def insere_meme_si_identique_tout(self,vals):
        for v in vals:
            self.insere_meme_si_identique(v)

def taille_arbre(arbre):
    taille_sag = taille_sad = 0
    if arbre.est_vide():
        return 0
    if arbre.left:
        taille_sag = taille_arbre(arbre.left)
    if arbre.right:
        taille_sad = taille_arbre(arbre.right)
    return 1 + taille_sad + taille_sag
'''
A = Node(17,Node(5),Node(22,Node(19),Node(28)))
B = Node(63,Node(45),Node(75,Node(68)))
C = Node(35,A,B)
#print(C.montrer())
'''
arbre = Node(18)
arbre.insere_tout([15,13,12,16,23,32,19,21])
#print(arbre)
#print(arbre.recherche(14))

arbre2 = Node(18)
arbre2.insere_meme_si_identique_tout([15,13,12,16,23,32,19,21,21])
print(arbre2)

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

def parcours_infixe(n):
    if n is None:
        return
    parcours_infixe(n.left)
    print(n.cle)
    parcours_infixe(n.right)

def parcours_prefixe(n):
    if n is None:
        return
    print(n.cle)
    parcours_prefixe(n.left)
    parcours_prefixe(n.right)

def parcours_suffixe(n):
    if n is None:
        return
    parcours_suffixe(n.left)
    parcours_suffixe(n.right)
    print(n.cle)

print("Parcours infixe")
parcours_infixe(arbre2)
print("Parcours prefixe")
parcours_prefixe(arbre2)