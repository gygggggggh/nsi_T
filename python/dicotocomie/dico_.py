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

def rech_tricho_iter(tab,v):
    """Recherche trichotomique d'un élément dans un tableau trié
    tab: tableau trié
    v: élément à rechercher
    """
    n = len(tab)
    a = 0
    b = n-1
    while a <= b:
        m1 = a + (b-a)//3
        m2 = b - (b-a)//3
        if tab[m1] == v:
            return m1
        if tab[m2] == v:
            return m2
        if v < tab[m1]:
            b = m1-1
        elif v > tab[m2]:
            a = m2+1
        else:
            a = m1+1
            b = m2-1
    return -1

#print(rech_tricho_iter([1,2,3,4,5,6,7,8,9],5))

#rotation d'une image par la methode diviser pour mieux regner avec PIL

from PIL import Image

im = Image.open("python/dicotocomie/Icon_Einstein_256x256.png")
largeur, longueur = im.size
pixels_im = im.load()



def rotation_aux(px,x,y,t):
    if t > 0:
        t = t//2
        # rotation des 4 sous-images
        rotation_aux(px,x,y,t)
        rotation_aux(px,x+t,y,t)
        rotation_aux(px,x+t,y+t,t)
        rotation_aux(px,x,y+t,t)
        # deplacement des sous-images
        for i in range(t):
            for j in range(t):
                p0 = px[x+i,y+j] # on stock pixel carré 1 (supérieur gauche)
                px[x+i,y+j] = px[x+t+i,y+j] # on déplace pixel carré 2 (supérieur droit) dans pixel carré 1
                px[x+t+i,y+j] = px[x+t+i,y+t+j] # on déplace pixel carré 3 (inférieur droit) dans pixel carré 2
                px[x+t+i,y+t+j] = px[x+i,y+t+j] # on déplace pixel carré 4 (inférieur gauche) dans pixel carré 3
                px[x+i,y+t+j] = p0 # on déplace pixel carré 1 (supérieur gauche) dans pixel carré 4
def rotation(px,taille):
    rotation_aux(px,0,0,taille)

for i in range(4):
    rotation(pixels_im,largeur-10*i*2)
im.save("python/dicotocomie/Icon_Einstein_256x256_rot.png")


