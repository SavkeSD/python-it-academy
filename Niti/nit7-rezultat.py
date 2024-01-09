import threading  
import time 
  
obj1= threading.Condition() 
 
 
def task (): 
  
  print('addition of 1 to 100000000 ') 
  global add
  for i in range (1, 100000001):
      add = add+1 
  print('the condition object is releases now') 
    
add=0
#time.sleep(1)
t1 = threading.Thread(target = task) 
t2 = threading.Thread(target = task) 
t1.start() 
t2.start()
t1.join() 
t2.join()
print(add)
 
print("---------------------------")