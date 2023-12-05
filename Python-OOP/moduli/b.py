# import a
# from a import f1
from a import f1 as f
from a import f2

# from a import * ### ovo je da se importuje sve iz a


#a.f1()  ### kupi sve iz A, cak i onaj print("A"), iako smo mi eskplicitno rekli da samo pozove f-ju -->> ovo se zove samo kada ide import a

#f1()  ### kupi sve iz A, cak i onaj print("A"), iako smo mi eskplicitno rekli da samo pozove f-ju -->> ovako se poziva sa from a import f1, i kao sto vidimo nema a. pa f-ja



print(__name__)