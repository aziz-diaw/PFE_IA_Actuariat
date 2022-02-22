#### TERM INSURANCE CASE ###
import Actuariat.product as prod
import Actuariat.Reserves as res
import Actuariat.probabilities_one_insured as poi
import Table.tables

### ASSET ###


def V_t(x, n, m, i, table, t,C,isIA = False):
    if t==0:
        return 0
    else:
        if isIA :
            return res.nAx_reserve(x, n, m, i, table, t,C,True)
        else :
            return res.nAx_reserve(x, n, m, i, table,t,C,False)


def V_t_1(x, n, m, i, table, t,P,C,isIA = False) :
    if isIA :
        num = (V_t(x, n, m, i, table, t,C,True) + P) - C * poi.v(i) * poi.qx(x + t, table)
        denom = poi.v(i) * poi.px(x + t, table)
    else :
        num = (V_t(x, n, m, i, table, t,C) + P) - C*poi.v(i)*poi.qx(x+t,table)
        denom = poi.v(i)*poi.px(x+t,table)
    return num/denom


def premiums(x, n, m, i, table,C,isIA = False):
    if isIA:
        return prod.annual_nAx(x, n, m, i, table,C,True)
    else :
        return prod.annual_nAx(x, n, m, i, table,C)


def financial_income(Vt, P, i):
    return (Vt + P) * i


def last_premium_reserves(x, n, m, i, table, t, C,isIA = False):
    if isIA :
        return V_t(x, n, m, i, table, t,C,True)
    else :
        return V_t(x, n, m, i, table, t,C)


def total_ASSET(x, n, m, i, table, t, P,C,isIA = False):
    if isIA :
        return (V_t(x, n, m, i, table, t,C,True) + P) / poi.v(i)
    else :
        return (V_t(x, n, m, i, table, t,C) + P) / poi.v(i)




### LIABILITY ###


def claims(x, t, table, C):
    return poi.qx(x + t, table) * C


def premiums_reserves(x, n, m, i, table, t,P,C, isIA = False):
    if isIA :
        return poi.px(x + t, table) * V_t_1(x, n, m, i, table, t, P,C,True)
    else :
        return poi.px(x+t,table)*V_t_1(x, n, m, i, table, t,P,C)


def total_LIABILITY(x, n, m, i, table, t,P,C, isIA = False):
    if isIA :
        return claims(x, t, table,C) + premiums_reserves(x, n, m, i, table, t, P,C,True)
    else :
        return claims(x,t,table,C) + premiums_reserves(x, n, m, i, table, t,P,C)

# T = 4
# print(total_LIABILITY(50,5,5,0.01,Table.tables.TH_00_02,T,prod.annual_nAx(50,5,5,0.01,Table.tables.TH_00_02)))
# print(total_ASSET(50,5,5,0.01,Table.tables.TH_00_02,T,prod.annual_nAx(50,5,5,0.01,Table.tables.TH_00_02)))
