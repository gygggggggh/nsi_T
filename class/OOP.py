
from random import randint


class Chrono :
    def __init__(self, h, m, s) :
        self.h = h
        self.m = m
        self.s = s
        self._format()
        if self.h < 0 or self.h < 0 or self.s < 0 :
            raise ValueError("une date ne doit pas etre negatif ")
    def __str__(self):
        return f'{self.h}:{self.m}:{self.s}'
    
    def __repr__(self):
        return f'heure:{self.h}\nminute:{self.m}\nseconde:{self.s}'
    
    def _format(self) :
        self.m += self.s // 60
        self.s = self.s % 60
        self.h += self.m // 60
        self.m = self.m % 60
        
    def avancer(self, s) :
        self.s += s
        self._format()
        return self
        
    def __add__(self, s):
        return Chrono(self.h + s.h, self.m + s.m, self.s + s.s)
    
    def __sub__(self,s):
        return Chrono(self.h - s.h, self.m - s.m, self.s - s.s)
    
    def __mul__(self,k):
        return Chrono(self.h * k, self.m * k, self.s * k)
    
    def __rmul__(self, k):
        return self.__mul__(k)
    
    def __lt__(self, s):
        return self.h < s.h and self.m < s.m and self.s < s.s
    
    def __gt__(self, s):
        return self.h > s.h and self.m > s.m and self.s > s.s
    
    def __le__(self, s):
        return self.h <= s.h and self.m <= s.m and self.s <= s.s
    
    def __ge__(self, s):
        return self.h >= s.h and self.m >= s.m and self.s >= s.s
    
    def __eq__(self, s):
        return self.h == s.h and self.m == s.m and self.s == s.s
    
    def __ne__(self, s):
        return self.h != s.h and self.m != s.m and self.s != s.s
        
        

#print(Chrono(12, 39, 45).avancer(5))

#print(Chrono(0,0,1) - Chrono(0,0,2)) 

class Tableau:
    def __init__(self,imin,imax,v):
        self.imin = imin
        self.imax = imax
        self.tab = [v] * (imax - imin + 1)
    def __len__(self):
        return self.tab
    def __getitem__(self, i):
        if i < self.imin or i > self.imax :
            raise IndexError("index out of range",i)
        return self.tab[i - self.imin]
    def __setitem__(self, i, j):
        if i < self.imin or i > self.imax:
            raise IndexError("index out of range", i)
        self.tab[i - self.imin] = j
    def __str__(self):
        return str(self.tab)
        
t = Tableau( -10, 9, 4)

class TaBiDir:
    def __init__(self,g,d):
        self.g = g
        self.d = d
        self.tab = [randint(1,10)] * (g - d + 1)
    def imin(self):
        return self.g
    def imax(self):
        
        return self.d
    
    def append(self,v):
        
        self.d += 1
        self.tab.append(v)
    
    def prepend(self,v):
        self.g -= 1
        self.tab.insert(0,v)
    
    def __getitem__(self,i):
        return self.tab[i - self.g]
    
    def __setitem__(self,i,v):
        self.tab[i - self.g] = v
    
        

        
class Intervale:
    def __init__(self, a, b):
        if a > b:
            self.a = 0
            self.b = 0
        self.a = a
        self.b = b
    def est_vide(self):
        return self.a > self.b 
    def __len__(self):
        return self.b - self.a
    
    def __contains__(self, x):
        return self.a <= x <= self.b   
     
    def __eq__(self, i):
        return self.a == i.a and self.b == i.b
    
    def __le__(self, i):
        return self.a <= i.a and self.b <= i.b
    
    def intersection(self, i):
        if self.a > i.b or self.b < i.a:
            return Intervale(0,0)
        else:
            return Intervale(max(self.a, i.a), min(self.b, i.b))
        
    def union(self, i):
        return Intervale(min(self.a, i.a), max(self.b, i.b))
    
    def __str__(self):
        return f'[{self.a};{self.b}]'


# test de intersection
print(Intervale(1, 5).intersection(Intervale(5,6)))
print(Intervale(2,6).__contains__(4))
print(Intervale(1000, 0).union(Intervale(3, 9990)))
print(len(Intervale(1, 5)))


    