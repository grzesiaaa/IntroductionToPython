def triangle(start, end, symbol1, symbol2):
    for i in range(start, end,-2):
        if (i%4 == 1): 
            print(" " * int(0.5*(start-i)) + i*symbol2)
        if (i%4 == 3):
          print(" " * int(0.5*(start-i)) + i*symbol1)
   
print(triangle(7,0,'*', '+')) 
