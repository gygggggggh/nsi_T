

def depart(laby):
    for i in range(len(laby)):
        for j in range(len(laby[i])):
            if laby[i][j] == 2:
                return (i, j)

def adjacentes(i, j, laby):
    liste = []
    if i > 0 and laby[i-1][j] != 1 and laby[i-1][j] != 9:
        liste.append((i-1, j))
    if i < len(laby) - 1 and laby[i+1][j] != 1 and laby[i+1][j] != 9:
        liste.append((i+1, j))
    if j > 0 and laby[i][j-1] != 1 and laby[i][j-1] != 9:
        liste.append((i, j-1))
    if j < len(laby[i]) - 1 and laby[i][j+1] != 1 and laby[i][j+1] != 9:
        liste.append((i, j+1))
    return liste

print(adjacentes(1, 1, [[1, 1, 1], [9, 0, 0], [1, 0, 1]]))
    
def solution(laby):
    chemin = [depart(laby)]
    case = chemin[0]
    i = case[0]
    j = case[1]
    ad = adjacentes(i, j, laby)
    while ad != []:
        laby[i, j] = 9
        ad = adjacentes(i, j, laby)
        if ad != []:
            case = ad[0]
            chemin.append(case)
            i = case[0]
            j = case[1]
    return chemin


 
