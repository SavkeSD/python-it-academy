import sys

class Counter:
    
    def __init__(self,start=0,stop=sys.maxsize):
        self.start = start
        self.stop = stop
    
    #ovo je bila prvobitno get metoda
    def __iter__(self):   ### kada ima iter metodu i next, kazemo da je objekat ove klase ITERABILAN
        return self

    #ovo je bila prvobitno increment metoda
    def __next__(self):
        if self.start >= self.stop:
            print("The maximal value is reached.")
            raise StopIteration  ### ako ne stavimo ovo, ima da ide u infinite loop
        else:
            self.start += 1
        return self.start

# c = Counter(10,12)
# # print(c.get())
# c.increment()
# # print(c.get())
# c.increment()
# # print(c.get())
# c.increment()
# # print(c.get())
# c.increment()

obj = Counter(41,45)

# for message in obj: ### ovo mozemo da uradimo samo za iterabilne objekte
#     print(message)

print(next(iter(obj)))
print(next(iter(obj)))  
print(next(iter(obj)))  
print(next(iter(obj)))  
print(next(iter(obj)))  
print(next(iter(obj)))  



