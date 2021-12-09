import Actuariat.commutation_case_life as ccl
import Actuariat.product as prod
import numpy as np

## Life Annuities due at the End of year

# Up to the death
def ax(x, table, i):
    return ccl.Nx(x + 1, table, i) / (ccl.Dx(x, i, table))


# Temporary
def a_xn(x, n, i, table):
    return (ccl.Nx(x + 1, table, i) - ccl.Nx(x + n + 1, table, i)) / ccl.Dx(x, i, table)


# Deferred
def m_ax(x, m, i, table):
    return ccl.Nx(x + m + 1, table, i) / ccl.Dx(x, i, table)


# Temporary (n) and deferred (m)
def m_a_xn(x, n, m, i, table):
    return (ccl.Nx(x + m + 1, table, i) - ccl.Nx(x + m + n + 1, table, i)) / ccl.Dx(x, i, table)


## Life Annuities due at the beginning of year

# Up to the death
def _ax_(x, table, i):
    return ccl.Nx(x, table, i) / ccl.Dx(x, i, table)


# Temporary
def _a_xn_(x, n, i, table):
    return (ccl.Nx(x, table, i) - ccl.Nx(x + n, table, i)) / ccl.Dx(x, i, table)


# Deferred
def _m_ax_(x, m, i, table):
    return ccl.Nx(x + m, table, i) / ccl.Dx(x, i, table)


# Temporary (n) and deferred (m)
def _m_a_xn_(x, n, m, i, table):
    return (ccl.Nx(x + m, table, i) - ccl.Nx(x + m + n, table, i)) / ccl.Dx(x, i, table)


## Life Annuities with several payment each year, due at the end of the period

# Up to the death
def ax_k(x, table, i, k):
    return ax(x, table, i) + (k - 1) / (2 * k)


# Temporary
def a_xn_k(x, n, i, table, k):
    return a_xn(x, n, i, table) + ((k - 1) / (2 * k)) * (1 - ccl.nEx(x, n, i, table))


# Deferred
def m_ax_k(x, m, i, table, k):
    return m_ax(x, m, i, table) + ((k - 1) / (2 * k)) * ccl.nEx(x, m, i, table)


# Temporary (n) and deferred (m)
def m_a_xn_k(x, n, m, i, table, k):
    return ccl.nEx(x, m, i, table) * a_xn_k(x + m, n, i, table, k)


## Life Annuities with several payment each year, due at the beginning of the period

# Up to the death
def _ax__k(x, table, i, k):
    return _ax_(x, table, i) - (k - 1) / (2 * k)


# Temporary
def _a_xn__k(x, n, i, table, k):
    return _a_xn_(x, n, i, table) - ((k - 1) / (2 * k)) * (1 - ccl.nEx(x, n, i, table))


# Deferred
def _m_ax__k(x, m, i, table, k):
    return _m_ax_(x, m, i, table) - ((k - 1) / (2 * k)) * ccl.nEx(x, m, i, table)


# Temporary (n) and deferred (m)
def _m_a_xn__k(x, n, m, i, table, k):
    return ccl.nEx(x, m, i, table) * _a_xn__k(x + m, n, i, table, k)


def check_function_lan(x, n, m, i, table):
    a = m_a_xn(x, n, m, i, table)
    b = prod.nEx(x, m, i, table) * a_xn(x + m, n, i, table)
    resu1 = np.allclose(a, b)

    c = ax(x, table, i)
    d = m_ax(x, n, i, table) + a_xn(x, n, i, table)
    resu2 = np.allclose(c, d)

    e = _ax_(x, table, i)
    d = _m_ax_(x, n, i, table) + _a_xn_(x, n, i, table)
    resu3 = np.allclose(e, d)

    return resu1 == resu2 == resu3 == True

