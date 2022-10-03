from pile import Pile

def reverse_pile(*pile):
    '''revoie une pile avec les éléments dans l'ordre inverse de complexité temporelle 0(n*n)''' 
    pile = Pile(pile) 
    pile_reverse = Pile()
    old = pile.depiler()
    for i in range(len(pile)):
        old.append(pile.depiler())
    for i in old:
        pile_reverse.empiler(old[-i])
    return pile_reverse

print(reverse_pile(1,2,3,4,5,6,7,8,9,10))
