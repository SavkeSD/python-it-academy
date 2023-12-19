a = 4
b = 0

# if a == 3:
#     raise ZeroDivisionError
#     b = a/(a-3) 


# print(b)

# #####
# a = 3 
# try:
#     if a == 3:
#         raise ZeroDivisionError
#         b = a/(a-3)
#     print(b)
# except ZeroDivisionError:
#    print("An error occurred")

# ####

# a = [1,2,3]
# print("Element is : %d" %(a[3]))  ### ovo puca jer nema index 3 i avlja gresku "IndexError: list index out of range"

# try:
#     if a == 3:
#         # raise ZeroDivisionError
#         # b = a/(a-3)
#         pass
#     print(b)
#     a = [1,2,3]
#     print("Element is : %d" %(a[3]))
# except (ZeroDivisionError, IndexError):  ## ovako je ruzno resenje, jer uvek pokazuje na An error occurred bez obrzija koja od dve greske se javi, i to onda podelimo na 2 excepta
#    print("An error occurred")

# try:
#     if a == 3:
#         # raise ZeroDivisionError
#         # b = a/(a-3)
#         pass
#     print(b)
#     a = [1,2,3]
#     print("Element is : %d" %(a[3]))
# except (ZeroDivisionError):
#    print("ZeroDivisionError is  occurred")
# except(IndexError):
#     print("Index error is occurred")   

###############

# a = 3
# b = 0

# try:
#     if a == 3:
#         raise ZeroDivisionError
#         b = a/(a-3)
#     print(b)
# except(ZeroDivisionError):
#     print("ZeroDivisionError se javila")

# try:
#     a = [1,2,3]
#     print("Element is : %d" %(a[3]))
# except(IndexError):
#     print("IndexError se javio") 


####

a = 3
b = 0

try:
    print(x)  ### ovo baca name error
    if a == 3:
        raise ZeroDivisionError
        b = a/(a-3)
    print(b)
    a = [1,2,3]
    print("Element is : %d" %(a[3]))

except(ZeroDivisionError):
    print("ZeroDivisionError se javila")
except(IndexError):
    print("IndexError se javio")
except(Exception):
    print("Javio se neobradjen exception --- BIG ERROR!!!")       

# help(NameError)  vidimo informacije o NameErroru





