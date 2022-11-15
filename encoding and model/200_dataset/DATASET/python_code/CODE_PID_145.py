def fun145(num):
    nums = num
    order = 0
    while num != 0:
        order = order + 1
        num = num // 10

    num = nums
    sum = 0
    while num != 0:
        digit = num % 10
        sum = sum + digit ** order
        num = num // 10

    if sum == nums:
        return 'Armstrong Number'
    else:
        return 'Not an Armstrong Number' 
