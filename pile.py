class Pile:
    def __init__(self, *args):
        self.pile = list(args)
        
    def __str__(self):
        return str(self.pile)

    def est_vide(self):
        return len(self.pile) == 0
    
    def empiler(self, x):
        self.pile.append(x)
        
    def depiler(self):
        if self.est_vide():
            raise MemoryError("Pile vide")
        return self.pile.pop()
    
    def __len__(self):
        return len(self.pile)
    

def bonne_parenthese(chaine):
    pile = Pile()
    for c in chaine:
        if c == "(":
            pile.empiler(c)
        elif c == ")":
            try:
                pile.depiler()
            except MemoryError:
                return False
    return pile.est_vide()

def bonne_parenthese_sans_pile(chaine):
    ouvert = 0
    for c in chaine:
        if c == "(":
            ouvert += 1
        elif c == ")":
            ouvert -= 1
            if ouvert < 0:
                return False
    return ouvert == 0
    

def NPI(chaine):
    pile = Pile()
    for c in chaine:
        if c == "+":
            pile.empiler(pile.depiler() + pile.depiler())
        elif c == "-":
            pile.empiler(pile.depiler() - pile.depiler())
        elif c == "*":
            pile.empiler(pile.depiler() * pile.depiler())
        elif c == "/":
            pile.empiler(pile.depiler() / pile.depiler())
        elif c == "^":
            pile.empiler(pile.depiler() ** pile.depiler())
        elif c == " ": # espace
            pass
        else:
            pile.empiler(int(c))
    return pile.depiler()


if "__main__" == __name__:
    print(NPI("2 2 + 2 ^"))
    PAREN = bonne_parenthese("()(())()")
    print(PAREN)

    bon = Pile(1, 2, 3, 4, 5).est_vide()

    print(bon.__str__())
