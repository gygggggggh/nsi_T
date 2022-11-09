class Node:
    def __init__(self,e = None,sag = None , sad = None):
        self.cle = e
        self.left = sag
        self.right = sad
        self.parent = None
    def est_vid(self):
        return self.cle is None
    
    def est_feuille(self):
        return self.left is None and self.right is None

    def racine(self):
        return self.cle
    
    def montre(self,tab=0):
        pass
    def taille(self):
        pass
    def hauteur(self):
        pass
    def hauteurArbre(self):
        pass
    def cheminement(self):
        pass
    def cheminementInterne(self):
        pass
    def cheminementExterne(self):
        pass

        