def posortuj_rosnaco(list):
    n = len(list)
    for i in range(n-1):
        for j in range(i+1,n):
            if list[j]<list[i]:
               list[j],list[i] = list[i], list[j]
    return list

def posortuj_malejaco(list):
    n = len(list)
    for i in range(n-1):
        for j in range(i+1,n):
            if list[j]>list[i]:
               list[j],list[i] = list[i], list[j]
    return list

def czy_posortowana(list):
    list1 = list[:] 
    posortuj_rosnaco(list1)
    list2 = list[:]
    posortuj_malejaco(list2)
    if (list1 == list or list2 == list): 
        return True
    else:
        return False
        
list = [1,2,3,4,8,5] 
print(czy_posortowana(list))     

list = [1,2,3,4]
print(czy_posortowana(list))

list = [9,8,7,6,5,4,3]
print(czy_posortowana(list))
