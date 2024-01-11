import threading
 
X = [[1,2,3],
    [4,5,6],
    [7,8,9]]
 
Y = [[9,8,7],
    [6,5,4],
    [3,2,1]]
 
result = [[0,0,0],
        [0,0,0],
        [0,0,0]]
 
 
class MyThread(threading.Thread):
 
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.i=i
 
    def run(self):
        print('running')
        print("Nit ",self.i)
        for j in range(len(X[i])):
            result[self.i][j]=X[self.i][j]+Y[self.i][j]
 
t = []
for i in range(len(X)):
    t.append(MyThread(i))
print(t)
for i in range(len(X)):
    t[i].start()
    t[i].join() # zakomentarisati
    #pass
 
for r in result:
    print(r)