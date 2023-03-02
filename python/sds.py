"""Voici un exemple d'arbre binaire de recherche dans lequel on a stocké dans cet ordre
les valeurs :
[26, 3, 42, 15, 29, 19, 13, 1, 32, 37, 30]
L'étiquette d'un nœud indique la valeur du nœud suivie du nom du nœud.
Les nœuds ont été nommés dans l'ordre de leur insertion dans l'arbre ci-dessous.
'29, noeud04' signifie que le nœud nommé noeud04 possède la valeur 29.

1. On insère la valeur 25 dans l'arbre, dans un nouveau nœud nommé nœud11.
Recopier l'arbre binaire de recherche étudié et placer la valeur 25 sur cet arbre
en coloriant en rouge le chemin parcouru.
Préciser sous quel nœud la valeur 25 sera insérée et si elle est insérée en fils
gauche ou en fils droit, et expliquer toutes les étapes de la décision
"""

# insert 25
[26, 3, 42, 15, 29, 19,25, 13, 1, 32, 37, 30,]
'''21-NSIJ1G11 Page : 8 /16
1. On insère la valeur 25 dans l'arbre, dans un nouveau nœud nommé nœud11.
Recopier l'arbre binaire de recherche étudié et placer la valeur 25 sur cet arbre
en coloriant en rouge le chemin parcouru.
Préciser sous quel nœud la valeur 25 sera insérée et si elle est insérée en fils
gauche ou en fils droit, et expliquer toutes les étapes de la décision.
2. Préciser toutes les valeurs entières que l’on peut stocker dans le nœud fils
gauche du nœud04 (vide pour l'instant), en respectant les règles sur les arbres
binaires de recherche ?
3. Voici un algorithme récursif permettant de parcourir et d'afficher les valeurs de
l'arbre :
Parcours(A) # A est un arbre binaire de recherche
Afficher(A.valeur)
Parcours(A.fils_gauche)
Parcours(A.fils_droit)
3.a. Écrire la liste de toutes les valeurs dans l'ordre où elles seront affichées.'''