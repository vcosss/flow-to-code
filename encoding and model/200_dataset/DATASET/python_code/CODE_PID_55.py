def fun55(choice, P, R, T):
    if choice == 1:
        A = P * ((1 + R / 100) ** T)
        I = A - P
    else:
        I = P * R * T / 100
    return I
