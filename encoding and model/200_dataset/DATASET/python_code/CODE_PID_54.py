def fun54(len1, len2, len3):
    if len1 == len2 == len3:
        return 'EQUILATERAL TRIANGLE'
    elif len1 == len2 or len2 == len3 or len3 == len1:
        return 'ISOSCELES TRIANGLE'
    else:
        return 'SCALENE TRIANGLE'