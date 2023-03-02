




class Cellule :
    def __init__(self ,valeur ,suivant):
        self.valeur = valeur
        self.suivant = suivant
    def __repr__( self ):
        return str(self.valeur)

c3 = Cellule ( " C " , None )
c2 = Cellule ( " B " , c3 )
c1 = Cellule ( " A " , c2 )

nav = c1
while nav is not None:
    #print (nav)
    nav = nav.suivant


class ListeChainee:
    def __init__(self):
        self._tete = None
        self._queue = None
        
    def __repr__(self):
        nav = self._tete
        chaine = ""
        while nav is not None:
            chaine += str(nav.valeur) + " -> "
            nav = nav.suivant
        if self.est_vide():
            chaine += "Vide"
        return chaine
    
    def prepend(self, valeur):
        c = Cellule(valeur, self._tete)
        if self.est_vide():
            self._queue = c
        self._tete = c
        
    def est_vide(self):
        return  not self._tete
    
    def pop(self):
        if not  self.est_vide():
            v = self._tete.valeur
            self._tete = self._tete.suivant
            if self._tete is None:
                self._queue = None
            return v
        else:
            raise IndexError("pop sur liste vide")
    def append(self,v):
        c = Cellule(v,None)
        if self.est_vide():
            self._tete = c
        else : 
             self._queue.suivant = c 
        self._queue = c
    
    def __len__(self):
        nav = self._tete
        longueur = 0
        while nav is not None:
            longueur += 1
            nav = nav.suivant
        return longueur
    
l = ListeChainee()
for i in [1,"a","t","15"]:
    l.prepend(i)
l.pop()
print(l)
l.append("z")
print(l)

p = ListeChainee()
print(p)

