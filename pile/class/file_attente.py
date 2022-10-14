from random import randint
from file import File

"""Terminale NSI Piles et Files
Un unique guichet ouvert 8h00 consécutives (soit 8 x 60 x 60 secondes). Les clients arrivent et font la
queue. La probabilité d’arrivée d’un nouveau client dans l’intervalle [t; t + 1[ est p.
Le temps que prend le service d’un client suit une loi uniforme sur [30; 300[. Les clients, s’ils attendent
trop longtemps, partent sans être servis. Leur patience est une loi uniforme sur [120; 1800[
Notre objectif est d’écrire une simulation informatique afin d’estimer le rapport clients repartis sans être
servis sur nombre total de clients, en fonction de la probabilité p.
La simulation est discrète. Durant la simulation, une variable tFree indique la date où le guichet sera
libre. À chaque seconde t, il faut :
• Faire un tirage aléatoire pour savoir si un nouveau client arrive.
• Si oui, ajouter le nouveau client (avec sa limite de temps) dans la file d’attente.
• Quand un client est disponible et que le guichet est libre (si t est supérieur à tFree).
◦ Extraire le client de la file.
◦ Vérifier qu’il est toujours là (sinon, passer au « client » suivant).
◦ Tirer aléatoirement un temps de traitement.
◦ Et ajuster tFree en conséquence"""


class File_attente:
    def __init__(self):
        attente = File()
        tFree = 0
        t = 0
        tMax = 8 * 60 * 60
        proba_service = self._proba_service()
        patience = self._patience()s
    def __str__(self):
        txt = ""
        for i in self.attente:
            txt += str(i) + " <- "
        return txt
    def _proba_service(self):
        self.proba_service = randint(30,301)
        return self.proba_service
    def _patience(self):
        self.patience = randint(120,1801)
        return self.patience    
    def est_vide(self):
        return self.attente == []
           
            
            
            
            
            
            
if __name__ == "__main__":
    file_a = File_attente()
    print(file_a)
        
        
