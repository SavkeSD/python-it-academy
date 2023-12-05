# import time  ### importujemo modul time, i onda su nam dostupne sve funkcionalnosti sto time ima

# time.sleep(2)

# print("Test")
# time.sleep(2)
# print("Test1")

# from time import time #### iz modula time, importujemo samo time, sto je dobro, jer ne importujemo sve vec samo sto nam treba
# print(time())

# from time import time as t_time
# from datetime import time as dt_time

#--------------------------#
### Primer sa casa ###

#print("A")

# def f1():
#     print("Ovo je f1 iz a")

# def f2():
#     print("Ovo je f2 iz a")    

# print("Pozvano iz ", __name__)    

# print(__name__)

# if __name__ == "__main__":  ### ovo se poziva samo ako runujemo file a.py
#     print("Trava raste")

### from a import *
### from c import *

### i sada ako pozovemo f-ju foo() koja je definisana i u a i u c, onda ce se pozvati foo() f-ja iz c-a, jer je on najskoriji