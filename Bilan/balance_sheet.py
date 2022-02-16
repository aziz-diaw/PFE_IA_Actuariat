import xlsxwriter as xls
import Bilan.formulae as form
import Actuariat.product as prod
import Table.tables


def balance_sheet(x, n, m, i, table, t):
    P = prod.annual_nAx(x, n, m, i, table)
    workbook = xls.Workbook('Balance_sheet_for_Term_Insurance.xlsx')
    ws = workbook.add_worksheet("Balance Sheet")

    for T in range(0, t):
        prem = form.premiums(x, n, m, i, table)
        fin_inc = form.financial_income(form.V_t(x, n, m, i, table, T), P, i)
        if T == 0:
            lpr = 0
        else:
            lpr = form.last_premium_reserves(x, n, m, i, table, T)
        claims = form.claims(x,T,table)
        pr = form.premiums_reserves(x,n,m,i,table,T,P)
        tot_ass = form.total_ASSET(x,n,m,i,table,T,P)
        tot_lia = form.total_LIABILITY(x,n,m,i,table,T,P)

        ws.write(T + 6 * T, 0, "End of year" + str(T + 1))
        ws.write(T + 6 * T, 1, "BALANCE SHEET")
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

    workbook.close()

#
# x =50
# m = 5
# n = 5
# i = 0.01
# t = 5
# table = Table.tables.TH_00_02
# balance_sheet(x, n, m, i, table, t)
