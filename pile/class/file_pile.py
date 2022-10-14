
from pile import Pile

'''On peut utiliser la structure de pile existante pour implémenter une structure de file. Pour cela la
file contiendra deux piles : une pile pour les entrées (ajout des éléments à la file) et une pile pour
les sorties (retrait des éléments de la file). L’ajout se fait donc toujours sur la pile entrée et le retrait
sur la pile sortie. Si la pile sortie est vide on dépile un à un les éléments de la pile entrée pour les
empiler sur la pile sortie jusqu’à ce que le pile entrée soit vide. Un message d’erreur est généré si
la pile de sortie reste vide malgré le transfert des élément de la pile entrée.
Coder en python la classe File en utilisant cette implémentation'''

class File_avec_Pile:
    def __init__(self):
        self.entree = Pile()
        self.sortie = Pile()
        
    def ajouter(self, element):
        self.entree.empiler(element)
    def retirer(self):
        if self.sortie.est_vide():
            while not self.entree.est_vide():
                n = self.entree.depiler()
                self.sortie.empiler(n)
        for i in range(0, len(self.sortie)):
            delo = self.sortie.depiler()
            return delo
    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()
    def __str__(self):
        return str(self.entree) + str(self.sortie)
    def __len__(self):
        return len(self.entree) + len(self.sortie)
    

p1 = File_avec_Pile()
for v in [4,7,-2,3,8]:
        p1.ajouter(v)
             
print(p1)
print(p1.retirer())
print(p1.retirer())
print(p1)
