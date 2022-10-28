def porownaj(s1,s2):
    if len(s1) != len(s2):
        print ('False')
    elif s1.lower()==s2.lower():
        print ("True")
    else:
        print ("False")

print (porownaj('mapa', 'Mapa'))
