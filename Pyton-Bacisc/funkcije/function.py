
# a = 3
# b = 4
# c = a+b
# print(c)

# a : int = 3 ## kada hocemo da eksplicitno kazemo sta je
# b : int = 4
# c : int = a + b
# print(c)

# def ispis():
#     print("Ovo je telo funkcije.")
#     print("Ovo je telo funkcije, drugi red")

# def zbir():
#     a : int = 3
#     b : int = 4
#     c : int = a + b
#     print(c)

# def zbir2(a,b):
#     c = a + b
#     print(c)

# def zbir3(a,b):
#     c = a + b
#     return c

# def zbir4(a: int,b: int) -> int:  ### ova strelica znaci koji tip se ocekuje kao povratna vrednost
#     c: int = a + b
#     return c

# def zbir5(a: int,b: int) -> int:  ### ova strelica znaci koji tip se ocekuje kao povratna vrednost
#     return a + b

# def zbir6(a: int,b: int = 7) -> int:  ### ovo 7, znaci da je ovo podrazumevana vrednost, tj ako ne prosledimo vrednost b, b ce biti 7
#     return a + b

# def zbir7(a: int = 14,b: int = 7) -> int:  ### defaultne vrednosti za a i b
#     return a + b

# def zbir8(*a):  ### prihvata proizvoljan broj argumenata
#     for i in a:
#         print(i)


# zbir()
# zbir2(5,6)
# zbir2(10,15)
# # zbir2(int(input("Unesi prvi broj: ")), int(input("Unesi drugi broj: ")))
# p = zbir3(11,3)
# print(p)
# p1 = zbir2(5,14)  ## Posto nema povratnu vrednost, onda je None
# print(p1)
# print(zbir3(10,15))

# print(zbir6(10))   ### ovde se podrazumeva da je drugi argument 7
# print(zbir6(1,2))

# print(zbir7())
# zbir8(1,2,3)

## Napraviti f-ju, koja prima 3 broja, i da vrati max

def max(a: float,b: float,c: float,) -> float:
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
def max1(a: float,b: float,c: float) -> float:
    return a if (a > b and a > c) else b if (b > a and b > c) else c

print(max(7,1,5))
print(max1(10,1,5))

### Suma prvih n brojeva

def suma(n: int) -> int:
    s = 0
    for i in range(n+1):
        s+=i
    return s    

print(suma(100))
print(suma(10000000))

def fun1():
    print("Ja sam fun1")

def fun2():
    print("Ja sam fun2")
    fun1()

def fun3():
    print("Ja sam fun3")
    fun2()
    fun1()

fun2()
print("\n")
fun3()

### Rekurzija ###
def f(n):
    if n ==0:
        return  ### zavrsava funkciju
    print("Nema kraja", n)
    f(n-1)

f(5)






