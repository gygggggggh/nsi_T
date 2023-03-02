'''Exercice 4 (4 points)
Cet exercice porte sur les arbres binaires et leurs algorithmes associés
La fédération de badminton souhaite gérer ses compétitions à l’aide d’un logiciel.
Pour ce faire, une structure arbre de compétition a été définie récursivement de la façon suivante :
un arbre de compétition est soit l’arbre vide, noté ∅, soit un triplet composé d’une chaîne de caractères
appelée valeur, d’un arbre de compétition appelé sous-arbre gauche et d’un arbre de compétition
appelé sous-arbre droit.
On représente graphiquement un arbre de compétition de la façon suivante :
"Kamel"
"Kamel" "Carine"
"Joris" "Kamel" "Carine" "Abdou"
∅ ∅ ∅ ∅ ∅ ∅ ∅ ∅
Pour alléger la représentation d’un arbre de compétition, on ne notera pas les arbres vides, l’arbre
précédent sera donc représenté par l’arbre A suivant :
"Kamel"
"Kamel" "Carine"
"Joris" "Kamel" "Carine" "Abdou"
Cet arbre se lit de la façon suivante :
— 4 participants se sont affrontés : Joris, Kamel, Carine et Abdou. Leurs noms apparaissent en
bas de l’arbre, ce sont les valeurs de feuilles de l’arbre.
— Au premier tour, Kamel a battu Joris et Carine a battu Abdou.
— En finale, Kamel a battu Carine, il est donc le vainqueur de la compétition.
Pour s’assurer que chaque finaliste ait joué le même nombre de matchs, un arbre de compétition a
toutes ces feuilles à la même hauteur.
Les quatre fonctions suivantes pourront être utilisées :
— La fonction racine qui prend en paramètre un arbre de compétition arb et renvoie la valeur
de la racine.
Exemple : en reprenant l’exemple d’arbre de compétition présenté ci-dessus, racine(A) vaut
"Kamel".
— La fonction gauche qui prend en paramètre un arbre de compétition arb et renvoie son sous-
arbre gauche.
Exemple : en reprenant l’exemple d’arbre de compétition présenté ci-dessus, gauche(A) vaut
l’arbre représenté graphiquement ci-après :
21-NSIJ1AN1 Page : 8/12
"Kamel"
"Joris" "Kamel"
— La fonction droit qui prend en argument un arbre de compétition arb et renvoie son sous-arbre
droit.
Exemple : en reprenant l’exemple d’arbre de compétition présenté ci-dessus, droit(A) vaut
l’arbre représenté graphiquement ci-dessous :
"Carine"
"Carine" "Abdou"
— La fonction est_vide qui prend en argument un arbre de compétition et renvoie True si l’arbre
est vide et False sinon.
Exemple : en reprenant l’exemple d’arbre de compétition présenté ci-dessus, est_vide(A)
vaut False
Pour toutes les questions de l’exercice, on suppose que tous les joueurs d’une même compétition ont
un prénom 

On considère l’arbre de compétition B suivant :
"Lea"
"Lea" "Louis"
"Lea" "Theo" "Louis" "Anne"
"Marc" "Lea" "Claire""Theo""Marie""Louis""Anne""Kevin"

'''


arbre = ["lea", ["lea", ["lea", ["marc", [], []], ["claire", [], []]], ["theo", ["marie", [], []], []]], ["louis", ["anne", [], []], ["kevin", [], []]]]

def gauche(arbre):
    '''(arbre) -> arbre
    Renvoie le sous-arbre gauche de l'arbre de compétition arbre.
    '''
    return arbre[1]

def droit(arbre):
    '''(arbre) -> arbre
    Renvoie le sous-arbre droit de l'arbre de compétition arbre.
    '''
    return arbre[2]

def racine(arbre):
    '''(arbre) -> str
    Renvoie la valeur de la racine de l'arbre de compétition arbre.
    '''
    return arbre[0]

def est_vide(arbre):
    '''(arbre) -> bool
    Renvoie True si l'arbre de compétition arbre est vide, False sinon.
    '''
    return arbre == []


def occurences(arbre, nom):
    '''(arbre, str) -> int
    Renvoie le nombre de fois que le joueur nom a joué dans l'arbre de compétition arbre.
    '''
    if est_vide(arbre):
        return 0
    elif nom == racine(arbre):
        return 1 + occurences(gauche(arbre), nom) + occurences(droit(arbre), nom)
    else:
        return occurences(gauche(arbre), nom) + occurences(droit(arbre), nom)

def occurences_iter(arbre, nom):
    '''(arbre, str) -> int
    Renvoie le nombre de fois que le joueur nom a joué dans l'arbre de compétition arbre.
    '''
    if est_vide(arbre):
        return 0
    else:
        compteur = 0
        pile = [arbre]
        while pile != []:
            arbre = pile.pop()
            if racine(arbre) == nom:
                compteur += 1
            if not est_vide(gauche(arbre)):
                pile.append(gauche(arbre))
            if not est_vide(droit(arbre)):
                pile.append(droit(arbre))
        return compteur

def nombre_de_matchs(arbre):
        '''(arbre) -> int
        Renvoie le nombre de matchs joués dans l'arbre de compétition arbre.
        '''
        if est_vide(arbre):
            return 0
        else:
            return 1 + nombre_de_matchs(gauche(arbre)) + nombre_de_matchs(droit(arbre))

def liste_joueurs(arbre):
    '''(arbre) -> list
    Renvoie la liste des joueurs qui ont participé à l'arbre de compétition arbre.
    '''
    if est_vide(arbre):
        return []
    elif  gauche(arbre) == [] and droit(arbre) == []:
        return [racine(arbre)]
    else:
        return liste_joueurs(gauche(arbre)) + liste_joueurs(droit(arbre))
    
# unit tests
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    # occurences
    print(occurences(arbre, "lea"))
    print(occurences(arbre, "marc"))
    print(occurences(arbre, "marie"))
    print(occurences(arbre, "kevin"))
    print(occurences(arbre, "toto"))
    
    # occurences_iter
    print(occurences_iter(arbre, "lea"))
    print(occurences_iter(arbre, "marc"))
    print(occurences_iter(arbre, "marie"))
    print(occurences_iter(arbre, "kevin"))
    print(occurences_iter(arbre, "toto"))
    
    # nombre_de_matchs
    print(nombre_de_matchs(arbre))
    
    # liste_joueurs
    print(liste_joueurs(arbre))
    doctest.
