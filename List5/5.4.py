import time
A = time.time()
def fib_iter(n):
    print(0)
    x = 1
    y = 1
    print(x)
    print(y)
    for i in range (n-3):
        x,y = y, x+y     
        print(y)
    
print(fib_iter(15))   
B = time.time()
print(A-B)
        

