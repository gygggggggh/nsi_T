
def cree_vect(x,y):
    v = x,y
    return v

def afficher_vect(u):
    return f'({u[0]};{u[1]})'


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
    return d

def k_vect(u,k):
    m = u[0] * k , u[1] * k
    return m

def est_collinaire(u,v):
    return u[0] * v[1] == u[1] * v[0]

################################################################################

def cree_fract(n,d):
    return [n,d]

def afficher_fract(f):
    return f'{f[0]}/{f[1]}'
    
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

class vecteur():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def afficher(self):
        return f'({self.x};{self.y})'
        
    def est_egal(self,v):
        return self.x == v.x and self.y == v.y
    
    def somme(self,v):
        return vecteur(self.x + v.x,self.y + v.y)
    
    def diff(self,v):
        return vecteur(self.x - v.x,self.y - v.y)
    
    def k(self,k):
        return vecteur(self.x * k,self.y * k)
    
    
#####################################################  
class fraction():
    def __init__(self,n,d):
        self.n = n
        self.d = d
        
    def afficher(self):
        if self.d == 1:
            return f'{self.n}'
        elif self.n == 0:
            return f'{self.n}'
        elif self.d < 0:
            self.d = self.d * -1
            return f'{self.n*-1}/{self.d}'
        else:
            return f'{self.n}/{self.d}'
        
        
    def est_egal(self,f):
        return self.n == f.n and self.d == f.d
    
    def somme(self,f):
        return fraction(self.n + f.n,self.d + f.d)
    
    def diff(self,f):
        return fraction(self.n - f.n,self.d - f.d)
    
    def k_produit(self,k):
        return fraction(self.n * k,self.d * k)
    def k_div(self,k):
        return fraction(self.n / k,self.d / k)
    
    def div(self,f):
        return fraction(self.n / f.n,self.d / f.d)
    
    def puissance(self,k):
        return fraction(self.n ** k,self.d ** k)
    
    def inverse(self):
        return fraction(self.d,self.n)
    
    def reduction(self):
        return fraction(self.n // self.pgcd_itera(),self.d // self.pgcd_itera())
    
    def pgcd_rec(self):
        a = self.n
        b = self.d
        if b == 0:
            return a
        else:
            return fraction(b,a % b).pgcd_rec()

    def pgcd_itera(self):
        a = self.n
        b = self.d
        while b != 0:
            t = b
            b = a % b
            a = t
        return a  
    
    def pgcm(self):
        a = self.n
        b = self.d
        return abs(a*b)//fraction.pgcd_rec((a,b))
    def fract2float(self):
        return round(self.n / self.d,self.n)

    
print(fraction(21,15).pgcm())






    
    