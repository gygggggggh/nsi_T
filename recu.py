#apprtien recu

def apartient(v,tab,i):
    if i == len(tab)-1:
        return v == tab[i]
    return v == tab[i] or apartient(v,tab,i+1)
        
    
