### 28.11.2023  pocetak OOPa ###

def unos():
    lst = []
    k = int(input("Unesi broj "))
    while(k!=0):
        lst.append(k)
        k = int(input("Unesi broj "))
    return lst
 
def sortiraj(lst):
    lst.sort(reverse=True)
    return lst
 
def ispis(lst):
    print("Lista je: ",end="")
    for i in lst:
        print(i,end=" ")
 
 
'''lista = unos()
lista = sortiraj(lista)
ispis(lista)'''
 
ispis(sortiraj(unos()))

