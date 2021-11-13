import Actuariat.commutation_case_life as ccl


## Life Annuities due at the End of year

# Up to the death
def ax(x, table, v):
    return ccl.Nx(x + 1, table, v) / ccl.Dx(x, v, table)


# Temporary
def a_xn(x, n, v, table):
    return (ccl.Nx(x + 1, table, v) - ccl.Nx(x + n + 1, table, v)) / ccl.Dx(x, v, table)


# Deferred
def m_ax(x, m, v, table):
    return ccl.Nx(x + m + 1, table, v) / ccl.Dx(x, v, table)


# Temporary (n) and deferred (m)
def m_a_xn(x, n, m, v, table):
    return (ccl.Nx(x + m + 1, table, v) - ccl.Nx(x + m + n + 1, table, v)) / ccl.Dx(x, v, table)


## Life Annuities due at the beginning of year

# Up to the death
def _ax_(x, table, v):
    return ccl.Nx(x, table, v) / ccl.Dx(x, v, table)


# Temporary
def _a_xn_(x, n, v, table):
    return (ccl.Nx(x, table, v) - ccl.Nx(x + n, table, v)) / ccl.Dx(x, v, table)


# Deferred
def _m_ax_(x, m, v, table):
    return ccl.Nx(x + m, table, v) / ccl.Dx(x, v, table)


# Temporary (n) and deferred (m)
def _m_a_xn_(x, n, m, v, table):
    return (ccl.Nx(x + m, table, v) - ccl.Nx(x + m + n, table, v)) / ccl.Dx(x, v, table)


## Life Annuities with several payment each year, due at the end of the period

# Up to the death
def ax_k(x, table, v, k):
    return ax(x, table, v) + (k - 1) / (2 * k)


# Temporary
def a_xn_k(x, n, v, table, k):
    return a_xn(x, n, v, table) + ((k - 1) / (2 * k)) * (1 - ccl.nEx(x, n, v, table))


# Deferred
def m_ax_k(x, m, v, table, k):
    return m_ax(x, m, v, table) + ((k - 1) / (2 * k)) * ccl.nEx(x, m, v, table)


# Temporary (n) and deferred (m)
def m_a_xn_k(x, n, m, v, table, k):
    return ccl.nEx(x, m, v, table) * a_xn_k(x+m, n, v, table, k)


## Life Annuities with several payment each year, due at the beginning of the period

# Up to the death
def _ax__k(x, table, v, k):
    return _ax_(x, table, v) - (k - 1) / (2 * k)


# Temporary
def _a_xn__k(x, n, v, table, k):
    return _a_xn_(x, n, v, table) - ((k - 1) / (2 * k)) * (1 - ccl.nEx(x, n, v, table))


# Deferred
def _m_ax__k(x, m, v, table,k):
    return _m_ax_(x, m, v, table) - ((k - 1) / (2 * k)) * ccl.nEx(x, m, v, table)


# Temporary (n) and deferred (m)
def _m_a_xn__k(x, n, m, v, table,k):
    return ccl.nEx(x, m, v, table) * _a_xn__k(x + m, n, v, table, k)