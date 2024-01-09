class Singleton:

    instanca = None

    def __init__(self):
        ### Virtualy private constructor ###
        if Singleton.instanca != None:
            raise Exception("This class is singleton!!")
        else:
            Singleton.instanca = self

    @staticmethod
    def instanciraj():

        if Singleton.instanca == None:
            Singleton()
        return Singleton.instanca

a = Singleton()
print(id(a))
b = Singleton()
print(id(b))

c = Singleton.instanciraj()
print(id(c))

d = Singleton.instanciraj()
print(id(d))
