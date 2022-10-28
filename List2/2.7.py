def fib(n):
    if n==1:
        print (0)
    elif n==2:
        print ([0,1])
    elif n==3:
        print([0,1,1])
    else:
        f = [0,1,1]
        for i in range(3,n):
            f.append(f[i-1] + f[i-2])
        return f

print(fib(20))
