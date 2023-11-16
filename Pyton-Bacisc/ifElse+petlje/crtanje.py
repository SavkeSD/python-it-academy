#### 16.11.2023 

### povecavanje i smanjivanje zvezdica

# n = 10
# i = znak = 1

# while(i>0):
#     for j in range(0,i):
#         print("*",end="")
#     if(i==n):
#         znak-=2
#     i+=znak
#     print()

### drugi nacin, sa mnozenjem i indikatorom
# n = 10
# i = znak = 1

# while(i>0):
#     for j in range(0,i):
#         print("*",end="")
#     if(i==n):
#         znak*=-1
#     i+=znak
#     print()

# print("Zdravo",end="")
# print("Dobar dan",end="")
# print("Cao svima\r",end="")
# print("Zdravo",end="")
# print("Dobar dan",end="")

## Carriage return, vracanje na pocetak reda bez new line

# import time
# target = 20
# x      = 1
# dir    = 1

# while True:
#     print("\r",end="")
#     j = 0
#     while j < target:
#         print("#" if x==j else " ",end="")
#         j+=1
#     if x==0 or x==target:
#         dir*=-1
#     x+=dir
#     time.sleep(0.05) 

#### Crtanje prozora
## i+j==n+1 se odnosi na kontra dijagonalu
## j==n or i==j se odnosi na obicnu dijagonalu
n = 13

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 or i==n or j==1 or j==n or i==j or i+j==n+1):
            print("*",end="")
        else:
            print(" ",end="")    
 
    print()