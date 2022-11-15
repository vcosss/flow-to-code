def fun42(x, y, z):
    if x > y and x > z:
        mx = x
    elif y > x and y > z:
        mx = y
    else:
        mx = z
    
    return mx