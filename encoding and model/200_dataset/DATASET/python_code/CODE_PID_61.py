def fun61(weight, height):
    bmi = weight / (height ** 2)
    if bmi >= 30:
        return 'Obesity'
    elif bmi >= 24.9:
        return 'Overweight'
    elif bmi >= 18.5:
        return 'Healthy'
    else:
        return 'Underweight'