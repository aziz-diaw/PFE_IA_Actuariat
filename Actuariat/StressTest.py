import Table.tables as table
import Actuariat.probabilities_one_insured as poi
import numpy as np
import Actuariat.product as prod


def qx_stressed(stress_rate, tab):
    qx = np.zeros(len(tab))
    for i in range(0, len(tab) - 1):
        qx[i] = poi.qx(i, tab) * (1 - stress_rate)
    qx[len(tab) - 1] = 1
    return qx


def lx_stressed(stress_rate, tab):
    qx_str = qx_stressed(stress_rate, tab)
    lx = np.zeros(len(tab))
    lx[0] = 100000
    for i in range(1, len(tab)):
        lx[i] = lx[i - 1] * (1 - qx_str[i - 1])
    return lx


def nAx_stress(x, i, n, stress_rate, tab):
    lx_stress = lx_stressed(stress_rate, tab)
    return prod.nAx(x, n, i, lx_stress)


#print(nAx_stress(24,0.03,20,0.25,table.TH_00_02))
print(lx_stressed(0.25, table.TH_00_02))