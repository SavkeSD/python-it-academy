n = 3

a = [0]*n
print(a)

def fun(n,a,i):
    if(i==n):
        print(a)
        return
    a[i] = 0
    fun(n,a,i+1)
    a[i] = 1
    fun(n,a,i+1)    
    a[i] = 2
    fun(n,a,i+1)  

fun(n,a,0)