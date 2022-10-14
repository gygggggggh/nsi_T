# mini project lemmings 

import os
from time import sleep

with open('cave.txt') as f:
    cave = f.readlines()

cave = list(cave)
print(cave)
class Jeu:
    def __init__(self, cave,x,y):
        self.cave = cave
        self.place(x,y)
        self.larg = len(cave[0])
        self.haut = len(cave)
        self.sac = {}
    def afficher(self,personnage):
        for i in range(len(cave)):
            for j in range(len(cave[i])):
                if i == self.y and j == self.x:
                    print(personnage,end='')
                else:
                    print(cave[i][j],end='')
            print('',end='')
            
            
    
    def place(self, x, y):
        if cave[y][x] == ' ':
            self.x = x
            self.y = y
        else:
            raise ValueError('Position non valide')
        
 
    def deplacer(self,dir):
        x,y = self.x,self.y
        match dir :
            case 'n' :self.place(self.x, self.y-1) and y-1> 0
            case 's' :self.place(self.x, self.y+1) and y+1< self.haut
            case 'e' :self.place(self.x+1, self.y) and x+1< self.larg
            case 'o' :self.place(self.x-1, self.y) and x-1> 0
            case _ :raise ValueError('Direction non valide')        
    def ramasser(self,obj):
        if obj in self.sac:
            self.sac[obj] += 1
        else:
            self.sac[obj] = 1
    def poser(self,obj):
        if obj in self.sac:
            if self.sac[obj] > 0:
                self.sac[obj] -= 1
            if self.sac[obj] == 0:
                del self.sac[obj]
            else:
                return None
        
        
cave_r = Jeu(cave,1,2)
p1 = Jeu(cave,1,2).place(1,2)
cave_r.deplacer('e')
cave_r.afficher('X')

chemin = "eeessooosseeeeeeeeeee"

for d in chemin:
    cave_r.deplacer(d)
    cave_r.afficher('X')
    sleep(0.11)
cave_r.ramasser("O")
print(cave_r.sac)
cave_r.poser("O")
print(cave_r.sac)
