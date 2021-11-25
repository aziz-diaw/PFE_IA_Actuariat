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
