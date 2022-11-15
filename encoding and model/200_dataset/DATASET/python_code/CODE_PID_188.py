def fun188(P, R, T):
    A = P * (1 + R / 100) ** T
    CI = A - P
    return CI