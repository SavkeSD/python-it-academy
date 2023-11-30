

def sugar(func):
    def wrapper():
        print("sugar")
        func()
    return wrapper   

def milk(func):
    def wrapper():
        print("Hot milk!!")
        func()
    return wrapper

@sugar
@milk
def coffee(variety="arabica"):
    print(variety) 

# coffee()
# milk(coffee)()

# nesto = milk(coffee)
# nesto()

# sugar(milk(coffee))()

coffee()
