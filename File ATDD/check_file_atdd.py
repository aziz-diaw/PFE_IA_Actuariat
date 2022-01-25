import pandas as pd
import Actuariat.product as pro
import Table.tables as table
import numpy as np

file = pd.read_excel("Capital_Differe_TDD_Primes.xlsm")
col = file.columns


age = col[8]  # age chiffre = 50
payment_m = file.loc[0].iloc[8]  # payment m = 5
term_n = file.loc[1].iloc[8] # n = 5
rate = file.loc[2].iloc[8] # rate = 0.01
amount = file.loc[3].iloc[8] # amount = 100


cap_diff_formule = pro.nEx(age,term_n,rate,table.TF_00_02)*amount  # 94.169 via formule
cap_diff_excel = file.loc[9].iloc[9] # single premium 94.169 via excel



print(np.allclose(cap_diff_formule,cap_diff_excel))

