from random import randint


def max2(a,b):
    if a<b:
        return b
    else:
        return a
#print(max2(4,10))

def max3(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else: 
        return c
#print(max3(4,10,3))

def triangle(a,b,c):
    return a+b>c and a+c>b and b+c>a
    
    
#print(triangle(3,2,4))

def triangle_rectangle(a,b,c):
    return a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + c**2 == b**2
#print(triangle_rectangle(4,2,4)) 

def triangle_isocele(a,b,c):
    return a ==b or b == c or a == c
        
#print(triangle_isocele(3,4,3))

def triangle_equi(a,b,c):
    return a == b == c
    
#print(triangle_equi(3,3,3))

def valide_date(j,h,m,s):
    return 0< h <24 and 0 < m < 600 and 0< s < 60

#print(valide_date(12,5,9,12))

def convert_duree(s):
    j,h,m, = 0,0,0
    while s >61:
        if s >=86400:
            j +=1
            s -=86400
        elif s >= 3600:
            h+=1
            s -=3600
        elif s >= 60:
            m +=1
            s -= 60
    return(j,h,m,s)
#print(convert_duree(7200))
def covert_duree_bis(s):
    j = s // 86400
    s = s % 86400
    h = s//3600
    m = s//60
    s = s % 60

def bissextile(a):
    return a % 4 == 0 and a% 100 != 0 or a%400 == 0 
        
#print(bissextile(2000))       

def bjoursannee(a):
    if bissextile(a):
        return 366
    else: 
        return 365
#ou return 366 if bissextile(a) else 365

#print(bjoursannee(2000))

def nbjoursmois(a,m):
    if m <= 7 and m % 2 == 0 and m != 2 :
        return 30
    if m <= 7 and m % 2 != 0 and m != 2 :
        return 31
    if m > 7 and m % 2 == 0 and m != 2 :
        return 31
    if m > 7 and m % 2 != 0 and m != 2 :
        return 30
    if m == 2:
        if bissextile(a):
            return 29
        else:
            return 28
    
#print(nbjoursmois(2004,4))

'''def nbjours(jn, mn, an, j, m, a):
    jours = 0
    jours += pass #for i in range(a-1)bjoursannee(a+1)
    jours += pass
    jours += pass
    return jours'''
#print(nbjours(17,9,2022,17,9,2022))

def somme(t):
    s = 0
    for i in t :
        s += i
    return s 
    
    
#print(somme([1,-2,4,89,100]))

def somme_interv(t,a,b):
    s = 0
    for i in range(a,min(b+1,len(t))):
        s += t[i]
    return s 

#print(somme_interv([1,4,6,14,35],1,3))

def occurrences(v, t):
    s = 0
    for i in t :
        if i == v:
            s += 1
    return s 
#print(occurrences(3,[3,3,3,3]))


def randint_tab():
    t = []
    for i in range(101):
        t.append(randint(1,1000))
    return t 

def rand_tab9():
    t = []
    for i in range(1001):
        t.append(randint(0,9))
    return t 

#print(rand_tab9())

def stats_mille_lancers():
    occurence = [0,]*10
    t = rand_tab9()
    for i in range(len(t)):
        if t[i] == 0:
          occurence[0] += 1
        if t[i] == 1:
              occurence[1] += 1
        if t[i] == 2:
              occurence[2] += 1
        if t[i] == 3:
              occurence[3] += 1
        if t[i] == 4:
              occurence[4] += 1
        if t[i] == 5:
              occurence[5] += 1
        if t[i] == 6:
              occurence[6] += 1
        if t[i] == 7:
              occurence[7] += 1
        if t[i] == 8:
              occurence[8] += 1
        if t[i] == 9:
              occurence[9] += 1
    return occurence 
     
def stats_mille_lancers_bis():
    tab = [randint(0,9) for i in range(1000)]
    occurrences = []
    for i in range(10):
        occurrences.append(occurrences(i, tab))
    return occurrences
#print(stats_mille_lancers_bis() )  

def stats_mille_lancers_opti():
    occurrences = [0]*10
    for i in range(1000):
        x = randint(0,9) 
        occurrences[x] += 1
    return occurrences
#print(stats_mille_lancers_opti())
    
    
def fibonacci(n):
    if n <= 0:
        return [0]
    fibo = [0, 1]
    while len(fibo) < n:
        suivant = fibo[len(fibo) - 1] + fibo[len(fibo) - 2]
        fibo.append(suivant)
    return fibo

    
print(fibonacci(30))


def copie(t):
    c = []
    for i in t :
        c.append(i)
    return t,c
#print(copie([1,2,3]))


def ajout(v, t):
    c = []
    for i in t :
        c.append(i)
    c.append(v)
    return t,c
#print(ajout(3,[1,2,3]))

def tableau_aleatoire(n, a, b):
    #return [randint(1,1000) for i in range(n)]
    t = []
    for i in range(n):
        t.append(randint(a,b))
    return t
#print(tableau_aleatoire(3,5,8))

def tableau_croissant(n):
    t = [1]
    for i in range(n):
        rand = randint(0,n)
        t.append(rand+t[i])
    return t
    
print(tableau_croissant(10))

#print([0]*10**8)

def somme(n):
    if n == 0:
        return 0
    else:
        return n + somme(n-1)

#print(somme(10))

def puissance(x,n):
    if n == 0:
        return 1
    else:
        return x * puissance(x,n-1)
     
#print(puissance(2.5,100))   

def puissance_double(x,n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        resultat = puissance_double(x,n//2)
        return resultat * resultat
    else:
        resultat = puissance_double(x,(n-1)//2)
        return x * resultat * resultat
print(puissance_double(3,42))

def echange(tab, i, j):
    for k in range(len(tab)):
        if k == i:
            old = tab[i]
            tab[i] = tab[j]
            tab[j] = old
    return tab
print(echange([1,2,30,5,2,5,5,13],1,6))
        

