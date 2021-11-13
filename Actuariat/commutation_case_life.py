def Dx(x, v, table):
    return (v ** x ) * table[x]


def Nx(x, table, v):
    N = 0
    w = len(table) - 1
    for i in range(0, w - x + 1):
        N += Dx(x + i, v, table)
    return N


def Sx(x, table, v):
    S = 0
    w = len(table) - 1
    for i in range(0, w - x + 1):
        S += Nx(x + i, v, table)
    return S


# Pure Endowment
def nEx(x, n, v, table):
    return Dx(x + n, v, table) / Dx(x, v, table)
