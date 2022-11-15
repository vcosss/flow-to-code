def fun137(num):
    limit = num // 2
    i = 1
    root = 0
    while i <= limit:
        if i * i <= num:
            root = i
    return root
