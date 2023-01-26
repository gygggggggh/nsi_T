import time
def fusion(T1,T2):
    T = []
    i = 0
    j = 0
    while i < len(T1) and j < len(T2):
        if T1[i] < T2[j]:
            T.append(T1[i])
            i += 1
        else:
            T.append(T2[j])
            j += 1
    while i < len(T1):
        T.append(T1[i])
        i += 1
    while j < len(T2):
        T.append(T2[j])
        j += 1
    return T

#print(fusion([1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]))

def tri_fusion(T):
    if len(T) <= 1:
        return T
    m = len(T)//2
    T1,T2= tri_fusion(T[:m]),tri_fusion(T[m:])

    return fusion(T1,T2)
debut = time.perf_counter()
tri_fusion([12,29,3,40,54,62,79,80,91]*1000)
fin = time.perf_counter()
print(fin-debut)
def tri_selection(T):
    for i in range(len(T)-1):
        m = i
        for j in range(i+1,len(T)):
            if T[j] < T[m]:
                m = j
        T[i],T[m] = T[m],T[i]
    return T
debut = time.perf_counter()
tri_selection([12,29,3,40,54,62,79,80,91]*1000)
fin = time.perf_counter()
print(fin-debut)


def tri_insertion(T):
    for i in range(1,len(T)):
        v = T[i]
        j = i
        while j > 0 and T[j-1] > v:
            T[j] = T[j-1]
            j -= 1
        T[j] = v
    return T
debut = time.perf_counter()
tri_insertion([12,29,3,40,54,62,79,80,91]*1000)
fin = time.perf_counter()
print(fin-debut)


tab = [12,29,3,40,54,62,79,80,91]*1000
debut = time.perf_counter()
tab.sort()
fin = time.perf_counter()
print(fin-debut)