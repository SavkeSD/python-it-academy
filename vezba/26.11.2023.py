def zbir(a: float, b: float) -> float:
    return a+b

print(zbir(2,3))

def faktorijelFor(a: int) -> int:
    p =1
    for i in range(1,a+1):
        p*=i
    return p

def faktorijelFor(a: int) -> int:
    p =1
    for i in range(a,0,-1):
        p*=i
    return p

print(faktorijelFor(5))

def rekurzija(n: int) -> int:
    if n == 0:
        return
    print("Nema kraja", n)
    rekurzija(n-1)

rekurzija(5)

def rekurzijaFaktorijel(n: int) -> int:
    if n == 1:
        return n
    else:
       return n*rekurzijaFaktorijel(n-1)



a = rekurzijaFaktorijel(5)
print(a)




