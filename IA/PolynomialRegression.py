import pandas
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


donnees = pandas.read_csv('combinaisons.csv',usecols=['age', 'nombre_payment' , 'maturite' , 'taux' , 'montant' ,'prime'])
X = donnees.drop("prime", axis=1)
X = X.values
Y= donnees['prime']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)


def opti_poly_degree(degree_max):
    r2 = []
    for i in range(1,degree_max):
        pol = PolynomialFeatures(degree = i)
        x_train = pol.fit_transform(X_train)
        model = LinearRegression()
        model.fit(x_train,Y_train)
        pred_Y = model.predict(x_train)
        r2.append(r2_score(Y_train, pred_Y))
    return r2


essaie = opti_poly_degree(15)
print(essaie)

