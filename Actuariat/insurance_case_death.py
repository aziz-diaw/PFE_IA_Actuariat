import Actuariat.commutation_case_life as ccl
import Actuariat.commutation_case_death as ccd

# Term Assurance, differed (m)
def m_n_Ax(x, n, m, i, table):
    return (ccd.Mx(x + m, i, table) - ccd.Mx(x + n + m, i, table)) / ccl.Dx(x, i, table)


# Whole life, differed (m)
def m_Ax(x, m, i, table):
    return ccd.Mx(x + m, i, table) / ccl.Dx(x, i, table)


# Term Insurance with increasing life annuities
def n_IA_x(x, n, i, table):
    return (ccd.Rx(x, i, table) - ccd.Rx(x + n, i, table) - n * (ccd.Mx(x + n, i, table))) / ccl.Dx(x, i, table)


# Term Insurance with decreasing life annuities
def n_DA_x(x, n, i, table):
    return (n * ccd.Mx(x, i, table) - (ccd.Rx(x + 1, i, table) - ccd.Rx(x + n + 1, i, table))) / ccl.Dx(x,i, table)

