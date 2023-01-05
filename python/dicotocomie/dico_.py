def rech_dicho_iter(tab,v):
    """Recherche dichotomique d'un élément dans un tableau trié
    tab: tableau trié
    v: élément à rechercher
    """
    n = len(tab)
    a = 0
    b = n-1
    while a <= b:
        m = (a+b)//2
        if tab[m] == v:
            return m
        elif tab[m] < v:
            a = m+1
        else:
            b = m-1
    return -1

def rech_dicho_rec(tab,a,b,v):
    """Recherche dichotomique d'un élément dans un tableau trié
    tab: tableau trié
    v: élément à rechercher
    a: indice de début de recherche
    b: indice de fin de recherche
    """
    if b < a :
        return -1
    m = (a+b)//2
    if tab[m] == v:
        return m
    if v < tab[m]:
        return rech_dicho_rec(tab,a,m-1,v)
    else:
        return rech_dicho_rec(tab,a,m+1,v)

def dicho_rec(tab,v):
    """Recherche dichotomique d'un élément dans un tableau trié
    tab: tableau trié
    v: élément à rechercher
    """
    return rech_dicho_rec(tab,0,len(tab)-1,v)

#print(rech_dicho_iter([1,2,3,4,5,6,7,8,9],5))
#print(dicho_rec([1,2,3,4,5,6,7,8,9],5))

