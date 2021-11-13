import Actuariat.probabilities_one_insured as poi


def Cx(x, v, table):
    return (v ** (x + 1)) * poi.dx(x, table)


def Mx(x, v, table):
    M = 0
    w = len(table) - 1
    for i in range(0, w - x + 1):
        M += Cx(x + i, v, table)
    return M


def Rx(x, v, table):
    R = 0
    w = len(table) - 1
    for i in range(0, w - x + 1):
        R += Mx(x + i, v, table)
    return R

