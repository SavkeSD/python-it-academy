 ###

def square(x):
    return x ** 2

def triple(x):
    return x ** 3

print(square(5))
my_func = square
print(my_func(7))

print(triple(5))


### Dekorator -- uzima se izvorni oblik f-je samo se malo izmeni, i na taj nacin izvorna f-ja se ne menja

def kvadrat():
    print("Kvadrat")

def krug():
    print("krug")    

def my_decorator(function_to_decorate):
    def wrapper_arround_original_function():
        print("I am a code running before original function")

        function_to_decorate()

        print("And i am the code that runs after")

    return wrapper_arround_original_function

my_decorator(kvadrat)()
my_decorator(krug)() 

@my_decorator   ### kada ovako stavimo, sa ovim et, menja se izvorno stanje kub f-je, i kada pozovemo sada kub, onda se ona dekorise. Ako nemamo ovo et, onda nema dekoracije
def kub():
    print("Kub")

my_decorator(kub)()

kub()

