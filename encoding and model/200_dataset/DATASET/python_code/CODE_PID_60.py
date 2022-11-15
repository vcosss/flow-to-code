def fun60(height):
    if height > 195:
        return 'Abnormal height'
    elif height > 165:
        return 'Tall'
    elif height > 150:
        return 'Average'
    else:
        return 'Short'