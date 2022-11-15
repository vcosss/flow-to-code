def fun59(x, y):
    if x >= 0 and y >= 0:
        return 'First Quadrant'
    elif x < 0 and y >= 0:
        return 'Second Quadrant'
    elif x < 0 and y < 0:
        return 'Third Quadrant'
    else:
        return 'Fourth Quadrant'