import Actuariat.life_annuities as la
import Actuariat.product as prod
import matplotlib.pyplot as plt
import Table.tables


def nAx_reserve(x, n,m, i, table, t, C,isIA = False):
    if isIA :
        A =C*prod.nAx(x + t, n - t, i, table) - prod.annual_nAx(x, n, m, i, table, C, True)*la._a_xn_(x + t, n - t, i, table)
        print(A)
        return A
    else :
        B=C*prod.nAx(x + t, n - t, i, table) - prod.annual_nAx(x,n,m,i,table,C,False) * la._a_xn_(x + t, n - t, i, table)
        print(B)
        return B

x=40
n=15
m=15
i=0.001
C=2000
t=1
#print(C*prod.nAx(x + t, n - t, i, Table.tables.TH_00_02))
#print(prod.single_nAx(x + t, n - t,m, i, Table.tables.TH_00_02,C,False))
#print(prod.single_nAx(x,n,m,i,Table.tables.TH_00_02,C,True))
#print(prod.annual_nAx(x,n,m,i,Table.tables.TH_00_02,C,False))


#nAx_reserve(50,5,5,0.01,Table.tables.TH_00_02,2,2000,True)
#nAx_reserve(50,5,5,0.01,Table.tables.TH_00_02,2,2000,False)

#
# plt.scatter(range(6),res)
# plt.xlabel("durée du contrat en année")
# plt.ylabel("Réserve")
# plt.title("Réserves que doit avoir l'assruance pour un Term Insurance d'une durée de 5 ans")
# plt.ylim(0,0.002)
# plt.show()