import math

def wykryj_kolizje(a,b,r1,c,d,r2):
    """Zwróć True jeśli kolizja między dwoma dyskami zachodzi.

    a,b -- współrzędne środka dysku1
    r1 -- promień dysku1
    c,d -- współrzędne środka dysku2
    r2 -- promień dysku2
    r1,r2 muszą być większe od 0
    """

    if r1<=0 or r2<=0:
        return "BŁĄD!. Promień musi byc większy od zera."
    elif math.sqrt((c-a)**2+(d-b)**2) < (r1+r2):
        return True
    else:
        return "Brak kolizji."

print(wykryj_kolizje(4,4,1,0,0,1)) 
print(wykryj_kolizje(4,4,1,0,0,5)) 
print(wykryj_kolizje(4,4,0,0,0,5))  



def przesun_dysk(s1,s2):
    """Przesuń dysk o środku w s1 o wektor s2 i zwróć nowe współrzędne środka.

    s1,s2 --  liczby zespolone
    """
    x = s1.real+s2.real
    y = s1.imag+s2.imag
    print("po przesunięciu dysk ma środek w punkcie:",'(', int(x),',', int(y),')')

print(przesun_dysk(1+1j,1+0j))
