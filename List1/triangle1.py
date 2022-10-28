def triangle():
    a = float(input("Podaj  długość pierwszego boku: "))
    b = float(input("Podaj długość drugiego boku: "))
    c = float(input("Podaj długośc trzeciego boku:"))
    if a <= 0 or b <= 0 or c <= 0:
         print("False")
    elif a+b>c and a+c>b and b+c>a:
           print("True")
    else:
        print("False")

print (triangle())
