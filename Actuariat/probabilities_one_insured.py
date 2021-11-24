import numpy as np

import Table.tables


def v(i):
    return 1 / (1 + i)


# Death between ages x and x + 1
def qx(x, table):
    if x >= len(table) - 1:
        return 1
    else:
        return (table[x] - table[x + 1]) / table[x]


# Probability of a life age x surviving to age x + 1
def px(x, table):
    if x >= len(table) - 1:
        return 0
    else:
        return 1 - qx(x, table)


def dx(x, table):
    if x >= len(table) - 1:
        return 0
    else:
        return table[x] - table[x + 1]


# Probability of a life age x surviving to age x + n
def npx(x, n, table):
    if x >= len(table) - 1:
        return 0
    return table[x + n] / table[x]


# Death between ages x and x + n
def nqx(x, n, table):
    return 1 - npx(x, n, table)


# Alive until m but not in m+1
def m_qx(x, m, table):
    return npx(x, m, table) - npx(x, m + 1, table)


# Alive until m but not in m+n
def m_n_qx(x, n, m, table):
    return npx(x, m, table) - npx(x, m + n, table)


def check_function_poi(x, n, m, table):
    a = npx(x, m + n, table)
    b = npx(x, m, table) * npx(x + m, n, table)
    resu1 = np.allclose(a, b)

    c = m_qx(x, m, table)
    d = npx(x, m, table) * qx(x + m, table)
    resu2 = np.allclose(c, d)

    e = m_n_qx(x, n, m, table)
    f = npx(x, m, table) * nqx(x + m, n, table)
    resu3 = np.allclose(e, f)

    return resu1 == resu2 == resu3 == True  # true car si les 3 sont faux ça return true


print(Table.tables.TD_88_90[-15],Table.tables.TD_88_90[92] )