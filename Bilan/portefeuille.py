import random
import numpy as np
import Bilan.formulae as form
import Actuariat.product as prod
import Table.tables
import Table.tables as table

taille = 500


def portefeuille(taille,table) :

    Client = liste_client(taille)
    prem_a  = np.zeros(1)
    fin_inc_a  = np.zeros(1)
    lpr_a = np.zeros(1)
    claims_a = np.zeros(1)
    pr_a = np.zeros(1)
    total_ass_a = np.zeros(1)
    total_lia_a = np.zeros(1)

    prem_ia = np.zeros(1)
    fin_inc_ia = np.zeros(1)
    lpr_ia = np.zeros(1)
    claims_ia = np.zeros(1)
    pr_ia = np.zeros(1)
    total_ass_ia = np.zeros(1)
    total_lia_ia = np.zeros(1)


    for c in range(Client.shape[0]) : # chaque portefeuille, on étale sur les années de blian qui doit etre inf ou egal aux max nombre de payment
        x = int(Client[c,0])
        n = int(Client[c,2])
        m = int(Client[c,1])
        i = Client[c,3]
        C = Client[c,4]
        #print(x,n,m,i,C)
        for T in range(0,int(min(Client[:,1]))): ## sur toute la taille de portefeuille
           #print(T)

            P = prod.annual_nAx(x, n, m, i, table, C, False)
            print(form.V_t(x, n, m, i, table, T, C, False))
            prem_a[0] += P ## somme des primes
            fin_inc = form.financial_income(form.V_t(x, n, m, i, table, T,C,False), P, i)
            fin_inc_a[0] += fin_inc # somme des fin_inc
            if T == 0:
                lpr = 0
                lpr_a[0] += lpr
            else:
                lpr = form.last_premium_reserves(x, n, m, i, table, T,C,False)
                lpr_a[0] += lpr
            claims = form.claims(x,T,table,C)
            claims_a[0] += claims
            pr = form.premiums_reserves(x,n,m,i,table,T,P,C,False)
            pr_a[0] += pr
            tot_ass = form.total_ASSET(x,n,m,i,table,T,P,C,False)
            total_ass_a[0] +=tot_ass
            tot_lia = form.total_LIABILITY(x,n,m,i,table,T,P,C,False)
            total_lia_a[0] += tot_lia


            P2 = prod.annual_nAx(x, n, m, i, table, C, True)
            prem2 = form.premiums(x, n, m, i, table, C, True)
            prem_ia[0]+=prem2
            fin_inc2 = form.financial_income(form.V_t(x, n, m, i, table, T, C, True), P2, i)
            fin_inc_ia[0] += fin_inc2
            if T == 0:
                lpr2 = 0
                lpr_ia[0] += lpr2
            else:
                lpr2 = form.last_premium_reserves(x, n, m, i, table, T, C, True)
                lpr_ia[0] += lpr2
            claims2 = form.claims(x, T, table, C)
            claims_ia[0]+= claims2
            tot_ass2 = form.total_ASSET(x, n, m, i, table, T, P2, C, True)
            total_ass_ia[0]+=tot_ass2
            tot_lia2 = form.total_LIABILITY(x, n, m, i, table, T, P2, C, True)
            total_lia_ia[0]+= tot_lia2
            pr2 = tot_lia2 - claims2
            pr_ia[0]+=pr2

    return prem_a,fin_inc_a ,lpr_a ,claims_a ,pr_a ,total_ass_a ,total_lia_a ,prem_ia ,fin_inc_ia ,lpr_ia , claims_ia ,pr_ia ,total_ass_ia ,total_lia_ia



def liste_client(taille):  # x , m , n , i , amount
    x = []  # Génération aléatoire des ages qui sera ajoutée

    for i in range(0, int(taille * 14 / 100) + 1):  # 14%
        x.append(random.randint(18, 24))
    for i in range(0, int(taille * 18 / 100) + 1):  # 18%
        x.append(random.randint(25, 34))
    for i in range(0, int(taille * 24 / 100) + 1):  # 24%
        x.append(random.randint(35, 44))
    for i in range(0, int(taille * 16 / 100) + 1):  # 16%
        x.append(random.randint(45, 54))
    for i in range(0, int(taille * 28 / 100) + 1):  # 28%
        x.append(random.randint(55, 106))
    Client = np.zeros((taille, 5))

    j = 0
    for i in range(0, taille):
        Client[i, j] = x[i]  # age

    j = 2
    for i in range(0, taille):
        if x[i] <= 30:
            Client[i, j] = random.randint(1, 42)  # on fait d'abord la maturité avant le nombre de payment
        elif x[i] > 30 and x[i] <= 45:
            Client[i, j] = random.randint(1, 35)
        elif x[i] > 45 and x[i] <= 55:
            Client[i, j] = random.randint(1, 20)
        elif x[i] > 55 and x[i] <= 65:
            Client[i, j] = random.randint(1, 20)
        else:
            Client[i, j] = random.randint(1, 15)

    j = 1
    for i in range(0, taille):
            Client[i, j] = random.randint(1, Client[i,2])  # nombre_de_payment on génére en max la maturité car impossibilité de la dépasser


    j = 3
    for i in range(0, taille):
        Client[i, j] = float(random.uniform(0.001, 0.02))  # taux d'intérêt

    j = 4
    for i in range(0, taille):
        Client[i, j] = random.randint(1000, 8000)  # amount

    return Client

random.seed(2)
print(portefeuille(2,table.TH_00_02))


