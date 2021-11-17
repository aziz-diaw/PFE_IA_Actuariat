import Actuariat.probabilities_one_insured as poi


def Cx(x, i, table):
    return (poi.v(i) ** (x + 1)) * poi.dx(x, table)


def Mx(x, i, table):
    M = 0
    w = len(table) - 1
    for j in range(0, w - x + 1):
        M += Cx(x + j, poi.v(i), table)
    return M


def Rx(x, i, table):
    R = 0
    w = len(table) - 1
    for j in range(0, w - x + 1):
        R += Mx(x + j, poi.v(i), table)
    return R

