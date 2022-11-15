def fun138(num):
    if num == 0:
        return 'Fibonacci Number'
    elif num == 1:
        return 'Fibonacci Number'
    else:
        a = 0
        b = 1
        c = 0
        while c < num:
            c = a + b
            a = b
            b = c
        
        if c == num:
            return 'Fibonacci Number'
        else:
            return 'Not a Fibonacci Number'
