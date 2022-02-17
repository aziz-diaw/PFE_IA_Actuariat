import Actuariat.commutation_case_life as ccl
import Actuariat.commutation_case_death as ccd
import Table.tables as tables
import Actuariat.probabilities_one_insured as poi


# Pure Endowment
def nEx(x, n, i, table):
    return ccl.Dx(x + n, i, table) / ccl.Dx(x, i, table)


# Whole Life
def Ax(x, i, table):
    return ccd.Mx(x, i, table) / ccl.Dx(x, i, table)


# Term Insurance
def nAx(x, n, i, table): # SINGLE PREMIUM
    return (ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table)) / ccl.Dx(x, i, table)


def annual_nAx(x,n,m,i,table):
    annual = 0
    for k in range(0,m):
        annual = annual + nEx(x,k,i,table)
    unique = nAx(x,n,i,table)
    return unique / annual


# Endowment
def Ax_n(C, x, n, i, table):
    return C * (ccl.Dx(x + n, i, table) + (ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table))) / ccl.Dx(x, i, table)


def Cx_n(C1, C2, x, n, i):
    a = C1 * nEx(x, n, i, tables.TF_00_02) + C2 * nAx(x, n, i, tables.TF_00_02)
    b = C1 * nEx(x, n, i, tables.TH_00_02) + C2 * nAx(x, n, i, tables.TH_00_02)
    return max(a, b)

