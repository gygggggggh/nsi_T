# mini project lemmings 
from random import randint

with open('cave.txt') as f:
    cave = f.readlines()



class Jeu:
    def __init__(self, cave, nb_lemmings):
        self.cave = cave
        self.nb_lemmings = nb_lemmings
        self.direction = ['>', '<', '^', 'v']
    
    def afficher(self):
        for i in cave : print(i.strip())
        return ''
    
    def creer_lemmings(self):
        if self.nb_lemmings == 0:
            return 'Aucun lemmings'
        else: 
            pass
            return self.afficher()
        
        
cave_r = Jeu(cave,2).creer_lemmings()
print(Jeu.afficher(cave_r))


        
