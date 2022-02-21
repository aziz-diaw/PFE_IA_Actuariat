import xlsxwriter as xls
import Bilan.formulae as form
import Actuariat.product as prod
import Table.tables


def balance_sheet(x, n, m, i, table, t,C):
    P = prod.annual_nAx(x, n, m, i, table,C,False)
    workbook = xls.Workbook('Balance_sheet_for_Term_Insurance_2.xlsx')
    ws = workbook.add_worksheet("Balance Sheet")

    for T in range(0, t):
        prem = form.premiums(x, n, m, i, table,C,False)
        fin_inc = form.financial_income(form.V_t(x, n, m, i, table, T,C,False), P, i)
        if T == 0:
            lpr = 0
        else:
            lpr = form.last_premium_reserves(x, n, m, i, table, T,C,False)
        claims = form.claims(x,T,table,C)
        pr = form.premiums_reserves(x,n,m,i,table,T,P,C,False)
        tot_ass = form.total_ASSET(x,n,m,i,table,T,P,C,False)
        tot_lia = form.total_LIABILITY(x,n,m,i,table,T,P,C,False)

        ws.write(T + 6 * T, 0, "End of year" + str(T + 1))
        ws.write(T + 6 * T, 1, "BALANCE SHEET WITH ACTUARIAT")
        ws.write(T + 1 + 6 * T, 1, "ASSET")
        ws.write(T + 1 + 6 * T, 3, "LIABILITY")
        ws.write(T + 2 + 6 * T, 1, "Premiums")
        ws.write(T + 2 + 6 * T, 2, prem)
        ws.write(T + 2 + 6 * T, 3, "Claims")
        ws.write(T + 2 + 6 * T, 4, claims)
        ws.write(T + 3 + 6 * T, 1, "Financial income")
        ws.write(T + 3 + 6 * T, 2, fin_inc)
        ws.write(T + 3 + 6 * T, 3, "Premium Reserves")
        ws.write(T + 3 + 6 * T, 4, pr)
        ws.write(T + 4 + 6 * T, 1, "Last Premium Reserves")
        ws.write(T + 4 + 6 * T, 2, lpr)
        ws.write(T + 5 + 6 * T, 1, "Total")
        ws.write(T + 5 + 6 * T, 2, tot_ass)
        ws.write(T + 5 + 6 * T, 4, tot_lia)

        second = 6
        P2 = prod.annual_nAx(x, n, m, i, table,C,True)
        prem2 = form.premiums(x, n, m, i, table,C,True)
        fin_inc2 = form.financial_income(form.V_t(x, n, m, i, table, T,C,True), P2, i)
        if T == 0:
            lpr2 = 0
        else:
            lpr2 = form.last_premium_reserves(x, n, m, i, table, T,C,True)
        claims2 = form.claims(x, T, table,C)

        tot_ass2 = form.total_ASSET(x, n, m, i, table, T, P2,C,True)
        tot_lia2 = form.total_LIABILITY(x, n, m, i, table, T, P2,C,True)
        pr2 = tot_lia2 - claims2

        ws.write(T + 6 * T, 0+second, "End of year" + str(T + 1))
        ws.write(T + 6 * T, 1+second, "BALANCE SHEET WITH IA")
        ws.write(T + 1 + 6 * T, 1+second, "ASSET")
        ws.write(T + 1 + 6 * T, 3+second, "LIABILITY")
        ws.write(T + 2 + 6 * T, 1+second, "Premiums")
        ws.write(T + 2 + 6 * T, 2+second, prem2)
        ws.write(T + 2 + 6 * T, 3+second, "Claims")
        ws.write(T + 2 + 6 * T, 4+second, claims2)
        ws.write(T + 3 + 6 * T, 1+second, "Financial income")
        ws.write(T + 3 + 6 * T, 2+second, fin_inc2)
        ws.write(T + 3 + 6 * T, 3+second, "Premium Reserves")
        ws.write(T + 3 + 6 * T, 4+second, pr2)
        ws.write(T + 4 + 6 * T, 1+second, "Last Premium Reserves")
        ws.write(T + 4 + 6 * T, 2+second, lpr2)
        ws.write(T + 5 + 6 * T, 1+second, "Total")
        ws.write(T + 5 + 6 * T, 2+second, tot_ass2)
        ws.write(T + 5 + 6 * T, 4+second, tot_lia2)




    workbook.close()


x =50
m = 5
n = 5
i = 0.01
t = 5
C = 2000
table = Table.tables.TH_00_02
balance_sheet(x, n, m, i, table, t,C)
