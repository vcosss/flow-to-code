def fun139(num):
    if num == 0:
        return 'Tribonacci Number'
    elif num == 1:
        return 'Tribonacci Number'
    elif num == 2:
        return 'Tribonacci Number'
    else:
        a = 0
        b = 1
        c = 2
        d = 0
        while d < num:
            c = a + b + c
            a = b
            b = c
            c = d
        
        if d == num:
            return 'Fibonacci Number'
        else:
            return 'Not a Fibonacci Number'
