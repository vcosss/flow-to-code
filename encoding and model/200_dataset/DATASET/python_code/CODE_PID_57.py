def fun57(basic):
    if basic < 20000:
        HRA = 0.16 * basic
        DA = 0.20 * basic
    else:
        HRA = 0.24 * basic
        DA = 0.30 * basic
    total = basic + HRA + DA
    return total