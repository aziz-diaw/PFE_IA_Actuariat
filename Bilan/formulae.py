#### TERM INSURANCE CASE ###
import Actuariat.product as prod
import Actuariat.Reserves as res
import Actuariat.probabilities_one_insured as poi
import Table.tables

### ASSET ###


def V_t(x, n, m, i, table, t):
    return res.nAx_reserve(x, n, m, i, table, t)


def V_t_1(x, n, m, i, table, t,P,C=1) :
    num = (V_t(x, n, m, i, table, t) + P) - C*poi.v(i)*poi.qx(x+t,table)
    denom = poi.v(i)*poi.px(x+t,table)
    return num/denom


def premiums(x, n, m, i, table):
    return prod.annual_nAx(x, n, m, i, table)


def financial_income(Vt, P, i):
    return (Vt + P) * i


def last_premium_reserves(x, n, m, i, table, t):
    if t == 0:
        return 0
    else :
        return V_t(x, n, m, i, table, t)


def total_ASSET(x, n, m, i, table, t, P):
    return (V_t(x, n, m, i, table, t) + P) / poi.v(i)

def total_ASSET_2(x, n, m, i, table, t, P):
    premiums(x,n,m,i,table) + financial_income(V_t(x, n, m, i, table, t),P,i)+last_premium_reserves(x,n,m,i,table,t)


### LIABILITY ###


def claims(x, t, table, C=1):
    return poi.qx(x + t, table) * C


def premiums_reserves(x, n, m, i, table, t,P):
    return poi.px(x+t,table)*V_t_1(x, n, m, i, table, t,P)


def total_LIABILITY(x, n, m, i, table, t,P):
    return claims(x,t,table) + premiums_reserves(x, n, m, i, table, t,P)

T = 2

print(total_LIABILITY(50,5,5,0.01,Table.tables.TH_00_02,T,prod.annual_nAx(50,5,5,0.01,Table.tables.TH_00_02)))
print(total_ASSET(50,5,5,0.01,Table.tables.TH_00_02,T,prod.annual_nAx(50,5,5,0.01,Table.tables.TH_00_02)))
# print(total_ASSET_2(20,2,2,0.01,Table.tables.TH_00_02,T,prod.annual_nAx(50,5,5,0.01,Table.tables.TH_00_02)))