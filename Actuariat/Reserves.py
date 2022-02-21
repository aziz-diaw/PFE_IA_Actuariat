import Actuariat.life_annuities as la
import Actuariat.product as prod
import matplotlib.pyplot as plt
import Table.tables


def nAx_reserve(x, n,m, i, table, t, C,isIA = False):
    if isIA :
        return C*prod.nAx(x + t, n - t, i, table) - prod.annual_nAx(x,n,m,i,table,C,True) * la._a_xn_(x + t, n - t, i, table)
    else :
        return C*prod.nAx(x + t, n - t, i, table) - prod.annual_nAx(x,n,m,i,table,C) * la._a_xn_(x + t, n - t, i, table)



# res = [ nAx_reserve(50,5,5,0.01,Table.tables.TH_00_02,i)  for i in range(6) ]
#
# plt.scatter(range(6),res)
# plt.xlabel("durée du contrat en année")
# plt.ylabel("Réserve")
# plt.title("Réserves que doit avoir l'assruance pour un Term Insurance d'une durée de 5 ans")
# plt.ylim(0,0.002)
# plt.show()