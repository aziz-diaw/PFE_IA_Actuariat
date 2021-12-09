import Actuariat.commutation_case_life as ccl
import Actuariat.commutation_case_death as ccd
import Table.tables as table


# Pure Endowment
def nEx(x, n, i, table):
    return ccl.Dx(x + n, i, table) / ccl.Dx(x, i, table)


# Whole Life
def Ax(x, i, table):
    return ccd.Mx(x, i, table) / ccl.Dx(x, i, table)


# Term Insurance
def nAx(x, n, i, table):
    return (ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table)) / ccl.Dx(x, i, table)


# TODO : Endowment and Combined :------------> Done


# Endowment
def Ax_n(C,x, n, i, table):
    return C * (ccl.Dx(x + n, i, table) + (ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table))) / ccl.Dx(x, i, table)


# Combined Endowment : ici, on va retourner le max entre les 2 tables
def Cx_n(C1, C2, x, n, i, tableliste):
    return (max((ccd.Mx(x, i, tableliste[0]) - ccd.Mx(x + n, i, tableliste[0])) / (
            ccl.Nx(x, tableliste[0], i) - ccl.Nx(x + n, tableliste[0], i)) * C1 + ccl.Dx(x + n, i,
                                                                                         tableliste[0]) / (
                        ccl.Nx(x, tableliste[0], i) - ccl.Nx(x + n, tableliste[0], i)) * C2,
                (ccd.Mx(x, i, tableliste[1]) - ccd.Mx(x + n, i, tableliste[0])) / (
                        ccl.Nx(x, tableliste[1], i) - ccl.Nx(x + n, tableliste[1], i)) * C1 + ccl.Dx(x + n, i,
                                                                                                     tableliste[
                                                                                                         1]) / (
                        ccl.Nx(x, tableliste[0], i) - ccl.Nx(x + n, tableliste[1], i)) * C2))


### Test fonction python combined

print(Cx_n(200, 100,  40, 20, 0.02, [table.TH_00_02, table.TF_00_02]))
