text = input("podaj tekst:")
def rot13(text):
    result = ""
    for x in text:
        c = ord(x)
        if c>=ord('a') and c<= ord('z'):
            if c > ord('m'):
                c -=13
            else:
                c+=13
        elif c>=ord('A') and c<= ord('Z'):
            if c > ord ('M'):
                c -=13
            else:
                c+= 13
        result+= chr(c)
    return result

print(rot13(text))
    
