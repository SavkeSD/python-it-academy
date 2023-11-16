### 16.11.2023
### Crtanje kvadrata

# h = 10

# for i in range(h):
#     for j in range(h):
#         print("*",end="")
#     print()

# ispis = "*"

# for i in range(h):
#     print(h*ispis)

### Trougao
# for i in range(h):
#     for j in range(i+1):
#         print("*",end="")
#     print()

### Trougao na drugi nacin

# s = "*"

# for i in range(1,h+1):
#     print(i*s)

###### Sirenje pa skupljanje  #
                              ##
                              ###
                              ##
                              #

## for i in range(1,int(h/2)): ##
##     for j in range(1,i+1):  ##
##         print("*",end="")   ## 
##     print()                 ##

## for i in range              ## Savke radio

# for i in range(1,h+1):
#     print(i*s)
# for i in range(h-1,0,-1):
#     print(i*s)


# i = 0

# while i<10:
#     print(i)
#     i+=1
# print(i)

# i = 1

# while i<10:
#     i+=2
#     if i==3:
#         continue
#     print(i)

## Zbir prvih 10 brojeva

# i = 1
# sum = 0
# suma = 0

# while i<11:
#     sum+=i
#     i+=1
# print(sum)

# for i in range(11):
#     suma+=i
# print(suma)

### Ispisati sumu parnih brojeva, preko obe petlje
# i = 0
# sum = 0
# suma = 0


# while i<11:
#     sum += i
#     i+=2
# print(sum)

# for j in range(0,11,2):
#     suma += j
# print(suma)

#### Ispisi ovo, # ## ### ####
s = ""

for i in range(1,5):
    s+="#"
    print(s,end=" ")
