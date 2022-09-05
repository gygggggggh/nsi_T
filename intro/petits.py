

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

def nbjours(jn, mn, an, j, m, a):
    jours = 0
    jours += bjoursannee(a) * (a-an)
    jours += (nbjoursmois(a,m)*(m-mn)) - (nbjoursmois(an,mn)*(mn-m)) 
    jours += j-jn
    return jours
#print(nbjours(17,9,2022,17,9,2022))

def somme(t):
    s = 0
    for i in t :
        s += i
    return s 
    
    
print(somme([1,-2,4,89,100]))

def somme_interv(t,a,b):
    s = 0
    for i in range(a,min(b+1,len(t))):
        s += t[i]
    return s 

print(somme_interv([1,4,6,14,35],1,3))

def occurrences(v, t):
    s = 0
    for i in t :
        if i == v:
            s += i 

