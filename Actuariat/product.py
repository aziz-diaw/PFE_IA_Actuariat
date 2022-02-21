import numpy
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.neighbors import KNeighborsRegressor

import Actuariat.commutation_case_life as ccl
import Actuariat.commutation_case_death as ccd
import Table.tables
import Table.tables as tables
import pandas
import Actuariat.probabilities_one_insured as poi


# Pure Endowment
def nEx(x, n, i, table):
    return ccl.Dx(x + n, i, table) / ccl.Dx(x, i, table)


# Whole Life
def Ax(x, i, table):
    return ccd.Mx(x, i, table) / ccl.Dx(x, i, table)


# Term Insurance
def nAx(x, n, i, table,C=1):  # SINGLE PREMIUM
    return ((ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table)) / ccl.Dx(x, i, table))*C


def annual_nAx(x, n, m, i, table, C=1,IA=False):
    annual = 0
    for k in range(0, m):
        annual = annual + nEx(x, k, i, table)

    if IA == True:
        donnees = pandas.read_csv('combinaisons.csv',
                                  usecols=['age', 'nombre_payment', 'maturite', 'taux', 'montant', 'prime'])
        X = donnees.drop("prime", axis=1)
        X = X.values
        Y = donnees['prime']
        X_train, _, Y_train, _ = train_test_split(X, Y, random_state=0)
        # pol = PolynomialFeatures(degree=5)
        # x_train = pol.fit_transform(X_train)
        # model = LinearRegression()
        model2 = KNeighborsRegressor(n_neighbors=1)
        model2.fit(X_train, Y_train)
        x_IA = numpy.array([[x, m, n, i, C]])
        # x_IA = pol.fit_transform(x_IA)
        unique = model2.predict(x_IA)
    else:
        unique = nAx(x, n, i, table,C) / annual
    return unique

def single_nAx(x, n, m, i, table, C=1,IA=False):
    annual = 0
    for k in range(0, m):
        annual = annual + nEx(x, k, i, table)

    if IA == True:
        donnees = pandas.read_csv('combinaisons.csv',
                                  usecols=['age', 'nombre_payment', 'maturite', 'taux', 'montant', 'prime'])
        X = donnees.drop("prime", axis=1)
        X = X.values
        Y = donnees['prime']
        X_train, _, Y_train, _ = train_test_split(X, Y, random_state=0)
        # pol = PolynomialFeatures(degree=5)
        # x_train = pol.fit_transform(X_train)
        # model = LinearRegression()
        model2 = KNeighborsRegressor(n_neighbors=1)
        model2.fit(X_train, Y_train)
        x_IA = numpy.array([[x, m, n, i, C]])
        # x_IA = pol.fit_transform(x_IA)
        unique = model2.predict(x_IA)*annual
    else:
        unique = nAx(x, n, i, table,C)
    return unique


# Endowment
def Ax_n(C, x, n, i, table):
    return C * (ccl.Dx(x + n, i, table) + (ccd.Mx(x, i, table) - ccd.Mx(x + n, i, table))) / ccl.Dx(x, i, table)


def Cx_n(C1, C2, x, n, i):
    a = C1 * nEx(x, n, i, tables.TF_00_02) + C2 * nAx(x, n, i, tables.TF_00_02)
    b = C1 * nEx(x, n, i, tables.TH_00_02) + C2 * nAx(x, n, i, tables.TH_00_02)
    return max(a, b)


# x = 50
# n = 5
# m = 5
# i = 0.01
# table = Table.tables.TH_00_02
# print(annual_nAx(x, n, m, i, table,2000,False))
# print(annual_nAx(x, n, m, i, table,2000, True))
