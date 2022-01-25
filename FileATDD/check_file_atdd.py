import pandas as pd
import Actuariat.product as pro
import Table.tables as table
import numpy as np


def check_atdd(filename_cap_dif = "Capital_Differe_TDD_Primes.xlsm", filename_temp_dec = "Temporaire_Deces_TDD_Primes.xlsm"):
    file_cap = pd.read_excel(filename_cap_dif)
    col_cap = file_cap.columns

    age_cap = col_cap[8]
    term_n_cap = file_cap.loc[1].iloc[8]
    rate_cap = file_cap.loc[2].iloc[8]
    amount_cap = file_cap.loc[3].iloc[8]

    cap_diff_formule = pro.nEx(age_cap, term_n_cap, rate_cap, table.TF_00_02) * amount_cap
    cap_diff_excel = file_cap.loc[9].iloc[9]

    file_temp = pd.read_excel(filename_temp_dec)
    col_temp = file_temp.columns

    age_temp = col_temp[8]
    term_n_temp = file_temp.loc[1].iloc[8]
    rate_temp = file_temp.loc[2].iloc[8]
    amount_temp = file_temp.loc[3].iloc[8]

    temp_dec_formule = pro.nAx(age_temp, term_n_temp, rate_temp, table.TH_00_02) * amount_temp
    temp_dec_excel = file_temp.loc[9].iloc[9]

    return np.allclose(cap_diff_formule, cap_diff_excel), np.allclose(temp_dec_formule, temp_dec_excel)
