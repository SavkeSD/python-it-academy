### Setovi, skupovi, dictionary, tulips, range

# s = "sunce"
# print(id(s))
# s+="kisa"
# print(id(s))

# ## Poenta je ovde da se pokaze da su stringovi imutabilni, i kada radimo concat istog stringa, to je u stvari novi string na novoj memorijskoj lokaciji

# print(s[0])

# s[0] = "A" #### ne moze, jer je string imutabilan tj nepromenljiv


### Lista

# lista = [2,3,4,5]

# print(lista)
# lista[2] = 7
# print(lista)
# print(lista[4])
# lista[4] = 3
# print(lista[4])
# print(lista)

# lista.append(5)
# print(lista)

# lista.pop() ### brise poslednji element liste 
# print(lista)
# lista.pop(0) ### brise od pocetka, tj elemnt sa indexom nula u ovom slucaju
# print(lista)


# lista = [i for i in range(0,10)]
# print(lista)
# lista.pop(4)
# print(lista)


# lst1 = [1,3,5,7,9]
# lst2 = [1,2,4,6,8]
# lst3 = []

# for i in lst1:
#     lst3.append(i)
# for j in lst2:
#     lst3.append(j)    

# print(lst3)

# lst3.sort()
# print(lst3)
# lst3.reverse()
# print(lst3)

## extend - spoji dve liste
## copy - kopirati istu listu na novu memorijsku lokaciju

##### 21.11.2023

# arr = ["Sam", "Dean", "Bobby"]

# for i in range(len(arr)):
#     print(arr[i], "is on index",i)

# for k,v in enumerate(arr):
#     print(v, "is on idex",k)

# lista = []
# print(lista)

# #### append dodaje na kraju liste, insert moze da doda na neki index odredjeni, idex daje poziciju tj index nekog elementa
# ### 

# lista.append(1)
# print(lista)

# lista2 = [3,4]
# lista.extend(lista2)
# print(lista)

# lista.insert(1,7)  ## na idex 1 postavlja se broj 7
# print(lista)
# lista.append(7)
# print(lista.count(1))  ### count, radi kao u excelu, broji koliko se puta ponavaljva neki element
# print(lista.count(7))

# print(lista.pop(3))

# lista.clear()   ### obrise sve elemente liste
# print(lista)


# lista = [3,6,2,7,7,9,9]

# for i in lista:
#     print(i, end=" ")

# lista[3] = 45
# print("\n",lista)

## zamena mesta sa pomocnom promenljivom
# a = 7
# b = 5
# # pom = a
# # a = b
# # b = pom

# # print(a,b)

# # ## zamena sa ugradjenom funkcijom
# # (a,b) = (b,a)

# ### zamena na 3ci nacin
# a = 7
# b = 5

# a = a-b # a = 2, b = 5
# b = a+b # a = 2 , b = 7
# a = b-a #  a = 5 , b = 7
# print(a,b)


# lista = [3,6,2,7,7,9,9]
# print(lista)

# pom = lista[1] ## pom = 6
# lista [1] = lista[3]
# print(lista)
# lista[3] = pom
# print(lista)

# (lista[3],lista[1]) = (lista[1], lista[3])
# print(lista)

# lista.sort()  
# print(lista)
# lista.reverse()
# print(lista)

# lista = [7,2,1,5,4,3]
# ### buble sort
# ### sortiranje po rastucem poretku
# for i in range(len(lista)-1):
#     for j in range(i+1,len(lista)):
#         if lista[i] > lista[j]:  ## ako ovde stavimo manje, onda ce biti sortiranje po opadajucem poretku
#             lista[i],lista[j] = lista[j],lista[i]
# print(lista)

# lista = [5,9,2,5,4,7,7]

# print(lista[2:5])  ### slicevi, ide od indexa 2 do indexa 5, sa tim sto index 5 ne uzima u obzir
# print(lista[:5]) 
# print(lista[:])  # kada se ne stavi krajni index, ide do kraja
# print(lista[3:])
# print(lista[2:5][:2])  ### uzme listu od indexa 2 do 5, i od tih elemenata ispise prva 2. Tako da krajnji ispis nije od indexa 2 do 5, nego prva 2 elementa od 2 do 5
# print(lista[:5][2])   #### uzme listu od indexa 0 do indexa 5 (ne uzima index 5), i onda od te liste vrati drugi index

# print(lista[1:6:2])  ### ovde je 2 korak, step,, kao u for loopu 
# print(lista[::]) ## cela lista

# ### Negativni indexi krecu sa desna od -1, pa onda -2 itd, do minus onog broja kolika je duzina liste

# print(lista[2:5]) 
# print(lista[-5:-2])

# print(lista[:-2])
# print(lista[-2:])

# print(lista[::-1]) ### reverzni poredak, ide unazad
# print(lista[2:5:-1])
# print(lista[2::-1]) ## reverzni poredak ide unazad, step -1
# print(lista[4:1:-1])
# print(lista[-2:-5:-1])
# print(lista[-5:-2])

# a = [1,2,3]
# b = [4,5,6]
# c = []

# for i in range(len(a)):
#     c.append(a[i]+b[i])
# c = [a[i]+b[i] for i in range(len(a))]  ## drugi nacin za c listu, kroz list comprehension

# print(c)

# print(c)

# lista = [i for i in range(1,10)]
# print(lista)

# parni = []
# neparni = []

### primer sa petljama
# for i in lista:
#     if i%2==0:
#         parni.append(i)
#     else: 
#         neparni.append(i)

### primer sa ternarnim operatorom

# for x in lista:
#     parni.append(x) if x % 2 == 0 else neparni.append(x)

### primer sa list comprehension
# lista = [i for i in range(1,10)]

# parni = [x for x in lista if x%2==0 ]
# neparni = [x for x in lista if x%2!=0]

# print(parni)
# print(neparni)

# lista_od_dve_petlje = [ (i,j) for i in range(3) for j in range(3)]
# lista_od_dve_petlje = [ (i,j) for i in range(3) for j in range(3) if i>j]

# print(lista_od_dve_petlje)


### Ispitati da li je palindrom

s = "AnaVoliMilovana"
s = s.lower()
print(s)

print(s[::-1])

# if s == s[::-1]:
#     print("Jeste palindrom")
# else:
#     print("Nije palindrom")

# print("Jeste palindrom") if s == s[::-1] else print("Nije palindrom")

### Palindrom kroz for petlju

for i in range(len(s)//2):
    if(s[i] != s[len(s)-1-i]):
        print("Nije Palindrom")
        break
else:  #### else koji ide uz for petlju, else se odradi kada se zavrsi for petlja. U ovom slucaju, ako se if ispuni, ici ce break, i onda else za for, nece da se izvrsi
    print("Jeste palindrom")    


