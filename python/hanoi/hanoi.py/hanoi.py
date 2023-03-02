# creation de l'affichage de la tour de hanoi en class en cli

class hanoi:
    def __init__(self, n):
        self.n = n
        self.tour1 = []
        self.tour2 = []
        self.tour3 = []
        for i in range(n, 0, -1):
            self.tour1.append(i)
        self.affichage()

    def affichage(self):
        print(self)
    
    def __str__(self):
        return "tour1: " + str(self.tour1) + " tour2: " + str(self.tour2) + " tour3: " + str(self.tour3)

    def deplacer(self, depart, arrivee):
        match depart:
            case 1:
                if arrivee == 2:
                    self.tour2.append(self.tour1.pop())
                elif arrivee == 3:
                    self.tour3.append(self.tour1.pop())

            case 2:
                if arrivee == 1:
                    self.tour1.append(self.tour2.pop())
                elif arrivee == 3:
                    self.tour3.append(self.tour2.pop())
            case 3:
                if arrivee == 1:
                    self.tour1.append(self.tour3.pop())
                elif arrivee == 2:
                    self.tour2.append(self.tour3.pop())
        self.affichage()
    

h = hanoi(3)
h.deplacer(1, 2)
h.deplacer(1, 3)
h.deplacer(2, 3)
h.deplacer(1, 2)
h.deplacer(3, 1)
h.deplacer(3, 2)
h.deplacer(1, 2)
h.deplacer(1, 3)
h.deplacer(2, 3)
h.deplacer(2, 1)
h.deplacer(3, 1)
h.deplacer(2, 3)

