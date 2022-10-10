from class.pile import Pile

def reverse_pile(*pile):
    pile = Pile(*pile)
    pile_inverse = Pile()
    for i in range(len(pile)):
        pile_inverse.empiler(pile.depiler())
    return pile_inverse
#print(reverse_pile(1,2,3,4,5,6,7,8,9,10))

def intervert(*pile):
    pass
#print(intervert(1,2,3,4,5,6,7,8,9,10))

