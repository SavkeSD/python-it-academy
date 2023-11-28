
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

# def max(a: float,b: float,c: float,) -> float:
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
    
# def max1(a: float,b: float,c: float) -> float:
#     return a if (a > b and a > c) else b if (b > a and b > c) else c

# print(max(7,1,5))
# print(max1(10,1,5))

# ### Suma prvih n brojeva

# def suma(n: int) -> int:
#     s = 0
#     for i in range(n+1):
#         s+=i
#     return s    

# print(suma(100))
# print(suma(10000000))

# def fun1():
#     print("Ja sam fun1")

# def fun2():
#     print("Ja sam fun2")
#     fun1()

# def fun3():
#     print("Ja sam fun3")
#     fun2()
#     fun1()

# fun2()
# print("\n")
# fun3()

# ### Rekurzija ###
# def f(n):
#     if n ==0:
#         return  ### zavrsava funkciju
#     print("Nema kraja", n)
#     f(n-1)

# f(5)


### 28.11.2023 ###

# def myFunction():
#     return 1,2,3

# a,b,c = myFunction()  ### ovde je primer kako moze da se odmah dodeli vrednostima sta f-ja vrati
# print(a,b,c)


# def f(*args):  ### Za neimenovane parametre
#     print(args[0] + args[1])

# f(2,3)

# def f(a,*args,**kw):
#     print(kw["msg"],(a*(args[0]+args[1]+args[2])))

# def f():
#     pass  ### samo postoji f-ja nista ne radi

# def f(a,b,c=0):   ## def f(a,b=3,c)  ---->> ovo ne moze, jer ide sdesna u levo za defoltne vrednosti
#     print(a,b,c)

# f(1,2,3)
# f(1,2)

def g(*args):
    print(args)

g(1,2,3)
g(1,2,3,4,5,6)

def h(a,b,*c):
    print(a,b,c)

h(3,4,7,9,2)   ### 7,9,2 ide u c

def h1(a,b,*c,**k): ## **k je imenovani parametar, i to se cuva u formi dictionary-ja
    print(a,b,c,k,k["s"])  ### k je ceo dictionary a k["s"] vraca value od keya "s"


h1(3,4,7,9,2,s="Dobar dan",s2="Dobro vece")

def Min(a,b): ### veliko min, da se zna da nije ugradjena f-ja min, tj da se razlikuje od keyworda
    return a if a<b else b

print(Min(4,3))

def Min(a: int, b: int) -> int:  ### isto kao i Min f-ja gore, samo sa predefinisam vrednostima
    return a if a<b else b

def Min2(*a: int) -> int:
    max = a[0]
    for i in a:
#    for i in range(1,len[a]): ### ako idemo preko duzine niza, a krecemo od indexa 1, da ne poredimo nulti index sa samim sobom, a uzeli smo da je max nulti index    
        # print (i,end="")
        # print(type(a)) ### vidimo da je tuple
        if i > max:
            max = i
    return max        

Min2(1,2,3)
print()   
Min2(1,2,3,4,5,5,6)
print() 
print(Min2(2,3,4,5,6))

import sys

def Min3(*a: int) -> int:
    max = -sys.maxsize -1
    for i in a:
        if i > max:
            max = i
    return max

print(Min3(5,6,7))

### rekurzivne f-je ###

def suma(*args: int) -> int:
    s: int = 0
    for i in args:
        s+= i
    return s

print(suma(1,2,3,4,5))

def suma_n(n): ### suma prvih n brojeva
    s = 0
    for i in range(1,n+1):
        s+=i
    return s

print(suma_n(10))
print(suma_n(100))


def f(n):
    if n==0:   ### uslov ispadanja iz rekurzije
        return
    
    print(n,end=" ")
    f(n-1)
    print(n,end=" ")  ### ovaj print se ne desava, dok f(n-1) se ne razresi

f(3)

def kako_hocemo3(*a:int) -> int: ### max sa slicevima
    m = a[0]
    for i in a[1:]:
        if i>m:
            m = i
    return m

maxi = kako_hocemo3(-4,-7)
print(maxi)



def parcici(a):
    if len(a) == 0:
        return
    print(a)
    parcici(a[1:])  ## ovo znaci da smanjuje stalno za prvi element
    # print(a)

def iteretivno_parcici(a):  ### iterativno resenje vs rekurzivno resenje(parcici f-ja), kako rekurzija stalno pravi nove stack framove, iterativno je jefitnije, memorijski gledano
    for i in range(len(a)):
        print(a[i:])    

a = [1,2,3,4,5]

parcici(a)
iteretivno_parcici(a)

### zadatak: rekurzivno resenje, suma prvih n 

def suma_r(n):
    if n == 0:
        return 0
    return n + suma_r(n-1)

print(suma_r(4))











