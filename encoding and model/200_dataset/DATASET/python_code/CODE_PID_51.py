def fun51(CP, SP):
    if CP > SP:
        return 'LOSS'
    elif SP > CP:
        return 'PROFIT'
    else:
        return 'NO PROFIT, NO LOSS'