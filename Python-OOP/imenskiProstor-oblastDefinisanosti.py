#### name spacing, oblast definisanosti, imenski prostor, to je sve isto
# name = "global"

# # def a():
# #     def b():
# #         print(name)
# #     b()

# # a()


# def a():
#     name = "enclosing"
#     def b():
#         print(name)
#     b()

# a()

# ### primer iz glave

# x = 9
# def fun():
#     x = 7 #### x je ovde lokalna promenljiva, a ovo je lokalni namespace ,a x = 9 je globalni imenski prostor
#     print(x)

# fun()
# print(x)

# x = 9
# def fun():
#     x = 0
#     x += 7 #### ovo ne moze ako ne kazemo x = neka vrednos (ovde smo uzeli 0), jer sada ne vidi globalno x, i sada radi sa lokalnim promenljivima
#     print(x)

# fun()
# print(x)

# x = 9
# def fun(x): ### ako prosledimo argument x, to je drugi nacin da resimo problem x+=7 kada ne vidi globalnu promenljivu
#     x += 7 #### ovo ne moze ako ne kazemo x = neka vrednos (ovde smo uzeli 0), jer sada ne vidi globalno x, i sada radi sa lokalnim promenljivima
#     print(x)

# fun(0)
# print(x)

# x = 9
# def fun():
#     global x ### ovo se odnosi na globalnu promenljivu x, tj kazemo x je globalna promenljiva
#     x += 7 #### ovo ne moze ako ne kazemo x = neka vrednos (ovde smo uzeli 0), jer sada ne vidi globalno x, i sada radi sa lokalnim promenljivima. Tj vidi ovu globalnu x, ali problem je sto hocemo da je uvecamo kao lokalnu, ali nismo je prvo inicijalizovali. Tj on nadje x kao lokalnu promenljivu, ali nije nasao koliko je, tj nije inicijalizovana
#     print(x)

# fun(0)
# print(x) ### ovo je x globalna promenljiva, i ne vidi x lokalnu promenljivu

# x = 9
# def fun():
#     x = 7
#     b = 3
#     print(x)
#     print(locals())  ## ispisuje sve lokalne promenljive, kao dictionary
#     print(locals()['b'])


# fun()
# print(x)
# print("----")
# x = 19 ### ovo ce u globals da dobije vrednost
# globals()['x'] = 999
# locals()['x'] = 123
# print(globals()) ## printa globalne promenljive

### kraj primera iz glave ###

# name = "global"
# def a():
#     name = "enclosing"
#     def b():
#         print(name)
#     b()

# a()

# name = "global"

# def a():
#     name = "enclosing"
#     def b():
#         name = "local"
#         print(globals()['name'])   ### dohvatamo sada varijablu globals
#         print(name)                ### ovde dohvatamo lokalnu promenljivu iz def b, sto je local
#     b()

# a()

# x = 9
# def uvecaj(x):
#     x +=1
#     return x


# uvecaj(x)
# print(x)

# x = uvecaj(x)
# print(x)

