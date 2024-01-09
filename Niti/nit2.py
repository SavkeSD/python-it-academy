import threading
import time

def run():
    while True:
        print("thread running")
        global stop_threads
        if stop_threads:
            break

stop_threads = False
t1 = threading.Thread(target=run)
t1.start()
time.sleep(1)  ### glavna nit spava, a t1 radi za to vreme, kada prodje ova jedna sec, stopira se
stop_threads = True
###t1.join()  ## ovo je poruka glavnoj niti da saceka da se sporedna nit zavrsi, pa da onda nastavi glavna nit
print('thread killed')
