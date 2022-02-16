import Actuariat.life_annuities as la
import Actuariat.product as prod



def nAx_reserve(x, n,m, i, table, t, C=1):
    return C*prod.nAx(x + t, n - t, i, table) - prod.annual_nAx(x,n,m,i,table) * la._a_xn_(x + t, n - t, i, table)



