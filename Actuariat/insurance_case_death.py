import commutation_case_life as ccl
import commutation_case_death as ccd
import probabilities_one_insured as poi


# Whole Life
def Ax(x, i, table):
    return ccd.Mx(x, poi.v(i), table) / ccl.Dx(x, poi.v(i), table)


# Term Assurance
def nAx(x, n, i, table):
    return (ccd.Mx(x, poi.v(i), table) - ccd.Mx(x + n, poi.v(i), table)) / ccl.Dx(x, poi.v(i), table)


# Term Assurance, differed (m)
def m_n_Ax(x, n, m, i, table):
    return (ccd.Mx(x + m, poi.v(i), table) - ccd.Mx(x + n + m, poi.v(i), table)) / ccl.Dx(x, poi.v(i), table)


# Whole life, differed (m)
def m_Ax(x, m, i, table):
    return ccd.Mx(x + m, poi.v(i), table) / ccl.Dx(x, poi.v(i), table)


# Term Insurance with increasing life annuities
def n_IA_x(x, n, i, table):
    return (ccd.Rx(x, poi.v(i), table) - ccd.Rx(x + n, poi.v(i), table) - n * (ccd.Mx(x + n, poi.v(i), table))) / ccl.Dx(x, poi.v(i), table)


# Term Insurance with decreasing life annuities
def n_DA_x(x, n, i, table):
    return (n * ccd.Mx(x, poi.v(i), table) - (ccd.Rx(x + 1, poi.v(i), table) - ccd.Rx(x + n + 1, poi.v(i), table))) / ccl.Dx(x, poi.v(i), table)
