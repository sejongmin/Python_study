x, y, w, s = map(int, input().split())

if w * 2 > s:
    if w > s:
        if x > y:
            time = y * s + ((x - y) // 2) * (2 * s) + ((x - y) % 2) * w
        else:
            time = x * s + ((y - x) // 2) * (2 * s) + ((y - x) % 2) * w
    else:
        if x > y:
            time = y * s + (x - y) * w
        else:
            time = x * s + (y - x) * w
        

else:
    time = (x + y) * w

print(time)