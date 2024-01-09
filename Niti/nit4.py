import threading
import time
import sys
 
def func():
    while True:
        time.sleep(0.5)
        print("Thread alive, and it will die on program termination")
 
t1 = threading.Thread(target=func)
t1.daemon = True  ### ovo znaci, kada se main nit zavrsi, odmah zavrsava i background nit. Sto znaci ako u backgroundu je neka infinite loop, ovo je terminira
#t1.setDaemon(True)
t1.start()
time.sleep(2)
print("----------------------")
sys.exit()