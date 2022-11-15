def fun62(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        return 'Roots are real and different'
    elif d < 0:
        return 'Roots are complex and different'
    else:
        return 'Roots are real and equal'
