def Newton(n, k):
    if not 0 <= k <= n:
        return 0
    b = 1
    for t in range(min(k, n-k)):
        b *= n
        b /= t+1
        n -= 1
    return int(b)
   
def printPascal(n) :   
    for line in range(0, n) : 
        for i in range(0, line + 1) : 
            print(Newton(line, i), " " , end = "")
        print()

print(printPascal(10))
