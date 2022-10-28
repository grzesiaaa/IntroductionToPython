def rgb_to_html(r,g,b):
    a=hex(r)
    x=hex(g)
    c=hex(b)
    return('#'+(a[2:]+x[2:]+c[2:]).upper())
   

print(rgb_to_html(255,255,255))
print(rgb_to_html(255,240,210))
