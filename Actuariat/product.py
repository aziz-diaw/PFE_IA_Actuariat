import Actuariat.commutation_case_life as ccl
import Actuariat.commutation_case_death as ccd


# Pure Endowment
def nEx(x, n, i, table):
    return ccl.Dx(x + n, i, table) / ccl.Dx(x, i, table)


# Whole Life
def Ax(x, i, table):
    return ccd.Mx(x, i, table) / ccl.Dx(x, i, table)


# Term Insurance
def nAx(x, n, i, table):
    return (ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table)) / ccl.Dx(x, i, table)

# TODO : Endowment and Combined
