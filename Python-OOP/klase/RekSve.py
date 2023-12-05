### ovo je koncept zvan back tracking, iliti pretraga sa vracanjem  -->> lavirint npr

n = 5

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