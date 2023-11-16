### Setovi, skupovi, dictionary, tulips, range

s = "sunce"
print(id(s))
s+="kisa"
print(id(s))

## Poenta je ovde da se pokaze da su stringovi imutabilni, i kada radimo concat istog stringa, to je u stvari novi string na novoj memorijskoj lokaciji

print(s[0])

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


lst1 = [1,3,5,7,9]
lst2 = [1,2,4,6,8]
lst3 = []

for i in lst1:
    lst3.append(i)
for j in lst2:
    lst3.append(j)    

print(lst3)

lst3.sort()
print(lst3)
lst3.reverse()
print(lst3)

## extend - spoji dve liste
## copy - kopirati istu listu na novu memorijsku lokaciju

