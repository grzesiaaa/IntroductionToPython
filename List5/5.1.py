def rgb_to_html(r,g,b):
        return '#' + ''.join(f'{i:02X}' for i in (r,g,b))

print(rgb_to_html(255,255,255))
print(rgb_to_html(255,240,210))
