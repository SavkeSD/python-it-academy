### Tuple ###
## Fiksne stvari koje se ne menjaju

a = (1,2)

print(type(a))
print(a)
print(a[1])

# a[1] = 56 ## ne moze, jer je tuple imutabilan

print(a.count(1)) ### kao i excel, broji koliko puta se neki element javlja u tuple-u

a = 2,3  ### ali bolje je pisati sa zagradama 
print(type(a))

a = (1)  ### ovo je int, jer tretira kada je sam element kao int, i onda stavimo a = (1,) i onda ga vidi kao tuple
b = ("s")  
print(type(a))
print(type(b))

(c,d) = (6,7)
print(c)

a = (1,1,2)
for i in range(len(a)):
    print(a[i], end="")
print()    


### Setovi, tj skupovi
## ne trpi duplikate, tj sastoji se od unique elemenata
## ali su unordered, i ne moze da se indeksno pristupa
## na dva nacina se mogu formirati, sa {} i sa set()
a = {4,4,5,5}
print(a)
a.add(7)
print(a)
a.add(7)
print(a)

a = set()
a.add(9)
print(a)
print(type(a))
print(type({5}))

c = {}
print(type(c))  ## posto nema elemenata, odlucuje da je skup

## Dictionary ###

d = {"poz":7}
print(type(d))
print(d["poz"])

e = {"poz",7}
print(type(e))

f = {"god":37,"ime":"pera","br stanje:": 1,"porodica":["mama","tata"]}
print(f["god"])
print(f["porodica"])
print(type(f["god"]))

f["info"] = 7
print(f)

f["god"]=39
print(f)

g = {"god":37,"ime":"pera","br stanje:": 1,"a":{"por":["mama","tata"]}}
print(g)
print(g["a"])
print(g["a"]["por"])
print(g["a"]["por"][0])


## Konverzija iz jedne sekvence u drugu

aa = (2,4,2,3,3,4)
print(a)
bb = list(aa)
print(type(bb))
print(bb)

cc = set(bb)
print(type(cc))
print(cc)






