class liste_double_chaine:
    def __init__(self,valeur,suivant,precedent):
        self.valeur = valeur
        self.suivant = suivant
        self.precedent = precedent
    def __repr__(self):
        return str(self.valeur)
    def __len__(self):
        nav = self
        longueur = 0
        while nav is not None:
            longueur += 1
            nav = nav.suivant
        return longueur
    def prepend(self,valeur):
        self.precedent = liste_double_chaine(valeur,self,None)
        self = self.precedent
    def append(self,valeur):
        nav = self
        while nav.suivant is not None:
            nav = nav.suivant
        nav.suivant = liste_double_chaine(valeur,None,nav)
    def pop(self):
        nav = self
        while nav.suivant is not None:
            nav = nav.suivant
        nav.precedent.suivant = None
    


        