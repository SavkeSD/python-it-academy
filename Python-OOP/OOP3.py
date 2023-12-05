### II cas, OOP

### ovo nije bas dobro, jer svi objekti ove klase, ce imati istu boju, brzini itd ###
class Auto:
    # pass  ## ako je prazna klasa
    brzina = 190
    boja = 'crvena'
    agregat = 'dizel'
    broj_mesta = 5

print(Auto.brzina)
print(Auto.broj_mesta)

yugo = Auto()
print(yugo.boja)

pezo = Auto()
print(pezo.boja)
### ###

class Auto2:   ## f-je u klasi se nazivaju metode
    def __init__(self,bojanka,brzina=150):  ### konstruktor, inicijalizator, ovo se poziva cim se napravi objekat ove klase. Uvek ima neki defaultni konsktruktor, ako ga mi eksplicitno ne definisemo
        ### ove __init__ sa donjim crtama, su magic metode
#        print("Prvi objekat")
        self.brzina = brzina
        self.boja = bojanka

    def pisi(self):  ## nasa metoda koju smo mi napravili, nije magic ili specijalna
        print("Opis: ",self.boja,self.brzina)

    def vrati_boju(self):
        return self.boja

    def __str__(self) -> str: ###  ToString Metoda, ovo kada radimo print objekat samo, sta da se ispise  ## Tako da ovde ne treba metoda pisi, al neka je zbog primera
        return "Osobine su : " + str(self.brzina) + "  " + self.boja 
    
    def postavi_boju(self, nova_boja):
        self.boja = nova_boja

print("",end="\n")

yugo2 = Auto2("plava",200)
print(yugo2.brzina)
print(yugo2.boja)
yugo2.pisi()
print(yugo2.vrati_boju())

print("",end="\n")

pezo2 = Auto2("crvena",150)
print(pezo2.brzina)
print(pezo2.boja)
pezo2.pisi()

print("",end="\n")

nn_auto = Auto2("siva",50)
print(nn_auto.brzina)
print(nn_auto.boja)
nn_auto.pisi()

print("",end="\n")
print("",end="\n")

print(yugo2)  ### Ovo vraca memorijsku lokaciju, jer na toj memorijskoj lokaciji je ova slozena promenljiva. Nece da vrati sve informacije, jer ne zna sta nam treba
print(yugo2.__dict__)   ### Ovo vraca sve atribute kao dict

yugo2.postavi_boju("metalik")
print(yugo2)

### Person primer ###
## Imamo 3 vrste metoda u klasama
### 1.) Konstruktor
### 2.) Klasna metoda
### 3.) Staticka metoda

class Person:
    origin_country = "Serbia"  ## klasna promenljiva

    def __init__(self,name,age,gender):  ### Konstruktor
        self.name = name
        self.age = age
        self.gender = gender

    @classmethod
    def metoda(cls, zemlja):  ## Klasna metoda, koja menja atribute na nivou klase
        cls.origin_country = zemlja

    @staticmethod
    def metoda2():   ### Staticka metoda, koja ne moze da menja ni lokalne ni klasne atribute
        print("Bilo sta")    

    def speak(self,words):
        print(f"{self.name} speaks {words}")

ana = Person("Ana Petrovic", 30,"f")
ana.speak("Zdravo")  

print(ana.origin_country)
print(Person.origin_country) ### klasna promenljiva

Person.metoda("Neka Zemlja")  ### ovo pozivamo klasnu metodu, i kada ovo uradimo, za sve objekte koji su napravljeni od ove klase, ce se promeniti, bez obzira dal su napravljeni pre ili posle poziva ove metode
print(Person.origin_country)

Person.metoda2()


### Nasledjivanje ###

class Person:
    origin_country = "USA"
    def __init__ (self, name, age, gender):
        self.name = name
        self.age= age
        self.gender = gender

    def speak(self,words):
        print(f"{self.name} speaks {words}")

class Employee(Person):   ### Ovde klasa employee nasledjuje klasu Person
    def __init__ (self,name,age,gender,salary,job_title):
        super().__init__(name,age,gender)   ### pozivanje konstruktora iz Persona
        self.salary = salary
        self.job_title = job_title

