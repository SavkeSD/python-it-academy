import Tacka as t
import pandas

t3 = t.Tacka()
#print(t3.__dict__)

print(t3)

t4 = t.Tacka(1,1)
t5 = t.Tacka(2,2)

print(t4.rastojanje(t5))

print(type(t3))

print(t4.jednake(t5))
print(id(t5))
print(id(t4))
## print(t4 == t5)  ### ovde poredi memorijske lokacije

print(t4==t5)
print(t4+t5)

t6 = t4 + t5
print(t6)

print(t.Tacka.counter)

