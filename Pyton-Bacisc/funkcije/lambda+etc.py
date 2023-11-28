### Lambda izrazi su u stvari f-je
### x --> 3x je u stvari f(x) = 3x
### skraceni zapis f-je, pa se samo jednom koristi i nema potrebe da se definise f-ja

def sum_number(a,b):
    return a + b

print(sum_number(2,3))

sum_number_lambda = lambda a, b: a + b
print(sum_number(2,3))

str1 = "GeeksforGeeks"
upper = lambda string: string.upper()
print(upper(str1))



# prosledjivanje f-je, tj kao parametar f-je stavljamo drugu neku f-ju

def myfunction(f):
    f("Hello World")

myfunction(print)

def myfunction2(f):
    return f("Hello World!")

print(myfunction2(len)) 

def moja(s):
    return s[3]

print(moja("Savke"))
print(myfunction2(moja))