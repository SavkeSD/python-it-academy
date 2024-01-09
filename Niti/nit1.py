import threading

def worker(num):
    ### thread worker function ###
    print("Worker: %s" % num)
    return

for i in range(25):
    t = threading.Thread(target=worker,args=(i,))
    t.start()

print("-------------")