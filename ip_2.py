


def nb2Lst(nb):
    lst = []
    while nb > 0:
        lst.append(nb % 256)
        nb = nb >> 8
    return lst[::-1]


def lst2nb(lst):
    for i in range(len(lst)-1):
        lst[i] = lst[i] << 8*(3-i)
    nb = sum(lst)
    return nb


def masque2nb(x):
    return ((1 << (x))-1 )<< (32-x)  # 2**n  = 1 << n decalage de n bits , si x = 24 alors 1 << 24 =  1000000000000000000000000 , 1<< 24 -1 = 111111111111111111111111 ((1<<24)-1)<<8(on ajoute 8 zero)= 11111111111111111111111100000000


sasie = input ("Entrez l'adresse sous la forme ****.****.****.****/xx: ")
adr,mask = sasie.split("/") # on separe l'adresse et le masque
lst_adress = adr.split(".") # on separe les octets de l'adresse
lst_adress = [int(x) for x in lst_adress] # on convertit les octets en entier
mask = int(mask) # on convertit le masque en entier
adresse = lst2nb(lst_adress) # on convertit l'adresse en nombre
masque = masque2nb(mask) # on convertit le masque en nombre
lst_masque = nb2Lst(masque) # on convertit le masque en liste

reseau =  adresse & masque
nb_equipement = 1<< (32- mask)
fin_reseau = reseau + nb_equipement -1

print("IP",sasie)
print("Masque reseau",lst_masque)
print("adresse reseau",nb2Lst(reseau))
print("plage reseau",nb2Lst(reseau),"->",nb2Lst(fin_reseau))
print("nombre d'equipement",nb_equipement-2)
end = ".".join([str(x) for x in nb2Lst(fin_reseau)])



