N = 6
matrice_Adj = [[False] * N for i in range(N)]

lst_adj = [[1,4],[0,3],[0,1,4],[2],[5]]

for k in range(N):
    for j in  lst_adj[k-1]:
        matrice_Adj[k][j] = True

def affiche(matrice):
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == True:
                print(1," ")
            else:
                print(0," ")
        print()
#affiche(matrice_Adj)


# Graphe représenté par une matrice d’adjacence
class Graphe1:
    """ graphe repr é sent é par une matrice d'adjacence
    où les sommets sont les entiers 0 ,1 ,... ,n -1 """

    def __init__ (self ,n):
        self.n = n
        self.mat_adj = [[ False ] * n for i in range(n)]
    
    def ajouter_arc(self,s1,s2):
        self.mat_adj[s1][s2] = True
    
    def arc(self,s1,s2):
        return self.mat_adj[s1][s2]
    def successeurs(self,s):
        success = []
        for i in range(self.n):
            if self.mat_adj[s][i]:
                success.append(i)
        return success
    def predecesseurs(self,s):
        pred = []
        for j in range(self.n):
            if self.mat_adj[j][s]:
                pred.append(j)
        return pred
    def affiche(self):

        for i in range(self.n):
            print(i,"->",end=" ")
            for j in range(self.n):
                if self.mat_adj[i][j]:
                    print(j,end=" ")
            print()
    def nb_sommets(self):
        return self.n
    def degre(self,s):
        return len(self.successeurs(s))
    def nb_arcs(self):
        nb = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.mat_adj[i][j]:
                    nb += 1
        return nb
    def suprimer_arc(self,s1,s2):
        if self.arc(s1,s2):
            self.mat_adj[s1][s2] = False
        

class graphe2:
      """ un graphe avec dictionnaire d'adjacence """
      def __init__(self):
          self.succes = {}
        
      def ajouter_sommets(self,s):
          if s not in self.succes:
              self.succes[s] = set()
      def ajouter_arc(self,s1,s2):
          self.ajouter_sommets(s1)
          self.ajouter_sommets(s2)
          self.succes[s1].add(s2)
      def arc(self,s1,s2):
            return s2 in self.succes[s1]
      def sommets(self):
            return list(self.succes)
      def voisins(self,s):
            return list(self.succes[s])
      def affiche(self):
            for s in self.succes:
                print(s,"{",end=" ")
                for v in self.succes[s]:
                    print(v,end=" ")
                print("}")
      def degre(self,s):
            return len(self.succes[s])
      def nb_arcs(self):
            return sum(self.degre(s) for s in self.succes)
      def suprimer_arc(self,s1,s2):   
            if self.arc(s1,s2):
                self.succes[s1].remove(s2)

    
# unit test
# if __name__ == "__main__":
#     g = Graphe1(5)
#     g.ajouter_arc(0,1)
#     g.ajouter_arc(0,2)
#     g.ajouter_arc(0,4)
#     g.ajouter_arc(1,2)
#     g.ajouter_arc(1,3)
#     g.affiche()
#     print(g.nb_sommets())
#     print(g.degre(0))
#     print(g.nb_arcs())
#     g.suprimer_arc(0,2)
#     g.affiche()
g2 = graphe2()
g2.ajouter_arc(0,1)
g2.ajouter_arc(0,2)
g2.ajouter_arc(0,8)
g2.ajouter_arc(1,2)
g2.ajouter_arc(0,2)
g2.ajouter_arc(0,4)
g2.ajouter_arc(1,2)
g2.affiche()
#     print(g2.degre(0))
#     print(g2.nb_arcs())
#     g2.suprimer_arc(0,2)
#     g2.affiche()

g = graphe2()
g.ajouter_arc("A","B")
g.ajouter_arc("A","C")
g.ajouter_arc("A","E")

def parcours (g ,vus ,s):
    """ parcours en profondeur depuis le sommet s (récursif ) """
    vus.append (s)
    for v in g. voisins (s):
        if v not in vus :
            parcours(g ,vus ,v)

vus = [] 
parcours(g ,vus ,"A")
print(vus)
print("H" in vus)
print("B" in vus)


