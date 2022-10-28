def triangle(start, end, symbol):
    for i in range (start, end, -2):
        print(" " * int(start-i) + i*symbol)

print(triangle(7, 0, '*'))
