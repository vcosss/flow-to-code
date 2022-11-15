def fun50(year):
    if year % 100 == 0 and year % 400 == 0:
        return 'LEAP YEAR'
    elif year % 4 == 0:
        return 'LEAP YEAR'
    else:
        return 'NOT A LEAP YEAR'