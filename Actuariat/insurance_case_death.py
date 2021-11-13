import commutation_case_life as ccl
import commutation_case_death as ccd


# Whole Life
def Ax(x, v, table):
    return ccd.Mx(x, v, table) / ccl.Dx(x, v, table)


# Term Assurance
def nAx(x, n, v, table):
    return (ccd.Mx(x, v, table) - ccd.Mx(x + n, v, table)) / ccl.Dx(x, v, table)


# Term Assurance, differed (m)
def m_n_Ax(x, n, m, v, table):
    return (ccd.Mx(x + m, v, table) - ccd.Mx(x + n + m, v, table)) / ccl.Dx(x, v, table)


# Whole life, differed (m)
def m_Ax(x, m, v, table):
    return ccd.Mx(x + m, v, table) / ccl.Dx(x, v, table)


# Term Insurance with increasing life annuities
def n_IA_x(x, n, v, table):
    return (ccd.Rx(x, v, table) - ccd.Rx(x + n, v, table) - n * (ccd.Mx(x + n, v, table))) / ccl.Dx(x, v, table)


# Term Insurance with decreasing life annuities
def n_DA_x(x, n, v, table):
    return (n * ccd.Mx(x, v, table) - (ccd.Rx(x + 1, v, table) - ccd.Rx(x + n + 1, v, table))) / ccl.Dx(x, v, table)
