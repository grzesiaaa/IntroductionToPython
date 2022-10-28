import time
A = time.time()
def fib_rek(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_rek(n-1) + fib_rek(n-2)


def fib_rek2(n):
    for i in range(n):    
        print(fib_rek(i))

print(fib_rek2(15))

B = time.time()
print(A-B)    



