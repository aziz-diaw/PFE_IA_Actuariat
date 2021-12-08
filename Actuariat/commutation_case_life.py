import Actuariat.probabilities_one_insured as poi
import Table.tables


def Dx(x, i, table):
    return (poi.v(i) ** x) * table[x]


def Nx(x, table, i):
    N = 0
    w = len(table) - 1
    for j in range(0, w - x + 1):
        N += Dx(x + j, i, table)
    return N


def Sx(x, table, i):
    S = 0
    w = len(table) - 1
    for j in range(0, w - x + 1):
        S += Nx(x + j, table, i)
    return S


# Pure Endowment
def nEx(x, n, i, table):
    return Dx(x + n, i, table) / Dx(x, i, table)


