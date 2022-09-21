from ast import If
from re import I


def cree_vect(x,y):
    v = x,y
    return v

def afficher_vect(u):
    print(f'({u[0]};{u[1]})')

def x_vect(u):
    return u[0]

def y_vect(u):
    return u[1]

def est_egal_vect(u,v):
    return u[0] == v[0] and u[1] == v[1]

def somme_vect(u,v):
    s = u[0] + v[0],u[1] + v[1]
    return s

def diff_vect(u,v):
    d = (u[0] - v[0]),(u[1] - v[1])
    return s

def k_vect(u,k):
    m = u[0] * k , u[1] * k
    return m

def est_collinaire(u,v):
    return u[0] * v[1] == u[1] * v[0]

################################################################################

def cree_fract(n,d):
    return [n,d]

def afficher_fract(f):
    print(f'{f[0]}/{f[1]}')
    
def n_f(f):
    return f[0]

def d_f(f):
    return f[1]

def est_egal_f(f1,f2):
    return f1[0] == f2[0] and f1[1] == f2[1]

def somme_f(f1,f2):
    s = f1[0] + f2[0],f1[1] + f2[1]
    return s

def diff_f(f1,f2):
    d = f1[0] - f2[0],f1[1] - f2[1]
    return d

def k_f(f,k):
    m = f[0] * k , f[1] * k
    return m

def div_f(f1,f2):
    d = f1[0] / f2[0], f1[1] / f2[1]
    return d

def inverse_f(f):
    i = f[1],f[0]
    return i

################################################################################

class Vecteur():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def afficher(self):
        print(f'({self.x};{self.y})')
        
    def est_egal(self,v):
        return self.x == v.x and self.y == v.y
    
    def somme(self,v):
        return Vecteur(self.x + v.x,self.y + v.y)
    
    def diff(self,v):
        return Vecteur(self.x - v.x,self.y - v.y)
    
    def k(self,k):
        return Vecteur(self.x * k,self.y * k)
    
    def est_collinaire(self,v):
        return self.x * v.y == self.y * v.x
    
class fraction():
    def __init__(self,n,d):
        self.n = n
        self.d = d
        
    def afficher(self):
        print(f'{self.n}/{self.d}')
        
    def est_egal(self,f):
        return self.n == f.n and self.d == f.d
    
    def somme(self,f):
        return fraction(self.n + f.n,self.d + f.d)
    
    def diff(self,f):
        return fraction(self.n - f.n,self.d - f.d)
    
    def k(self,k):
        return fraction(self.n * k,self.d * k)
    
    def div(self,f):
        return fraction(self.n / f.n,self.d / f.d)
    
    def inverse(self):
        return fraction(self.d,self.n)


    
    