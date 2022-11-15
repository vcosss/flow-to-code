def fun144(num):
    nums = num
    rev = 0
    while num != 0:
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
    
    if rev == num:
        return 'Palindrome Number'
    else:
        return 'Not a Palindrome Number'