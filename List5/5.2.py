def html_to_rgb(kolor):
    if len(kolor)==7:
        r = int(kolor[1:3],16)
        g = int(kolor[3:5],16)
        b = int(kolor[5:],16)
        return r,g,b

print(html_to_rgb('#FFFFFF'))
print(html_to_rgb('#FFF0D2'))
