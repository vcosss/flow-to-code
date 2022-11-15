def fun44(x, y, z):
    if x < y and x < z:
        mn = x
    elif y < x and y < z:
        mn = y
    else:
        mn = z
    
    return mn