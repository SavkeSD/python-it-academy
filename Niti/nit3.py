import threading
import time
 
# counts from 1 to 9
def func(number):
    for i in range(1, 10):
        time.sleep(0.01)
        print('Thread ' + str(number) + ': prints ' + str(number*i))
 
# creates 3 threads
for i in range(0, 30):
    thread = threading.Thread(target=func, args=(i,))
    thread.start()
    #thread.join()  ### ako ovo otkomentarisemo, kazemo da se sve ovo zavrsi pa onda da dodje main nit
    if i<15:  ### ovo znaci da prvih 15 se zavrsi, pa onda ide glavna
        thread.join()
 
 
print("------------------------") 