class Lista:

    def unos(self): ### kafa su f-je van klasa, nemaju ovo self a sada imaju
        lst = []
        k = int(input("Unesi broj "))
        while(k!=0):
            lst.append(k)
            k = int(input("Unesi broj "))
        return lst
    
    def sortiraj(self, lst):
        lst.sort(reverse=True)
        return lst
    
    def ispis(self, lst):
        print("Lista je: ",end="")
        for i in lst:
            print(i,end=" ")