import pandas
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

donnees = pandas.read_csv('combinaisons.csv', usecols=['age', 'nombre_payment', 'maturite', 'taux', 'montant', 'prime'])
X = donnees.drop("prime", axis=1)
X = X.values
Y = donnees['prime']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)


### Polynôme optimal ===> 5 ####

def opti_poly_degree(degree_max):
    r2 = []
    for i in range(1, degree_max):
        print("degrée : ", i)
        pol = PolynomialFeatures(degree=i)
        x_train = pol.fit_transform(X_train)
        x_test= pol.fit_transform(X_test)
        model = LinearRegression()
        model.fit(x_train, Y_train)
        pred_Y = model.predict(x_test)
        r2.append(r2_score(pred_Y,Y_test))
    return r2

#
# degre_pol = opti_poly_degree(10)
# print(degre_pol)
# print("le modèle polynomial qui fit le mieux nos donnés est un modèle de degré : ", np.argmax(degre_pol)+1)
# print("Le coeffcient r2 de ce modèle est : ", degre_pol[np.argmax(degre_pol)])
# plt.plot(range(1,10),degre_pol)
# plt.ylabel("Score de régression")
# plt.xlabel("degrés")
# plt.title("Score de régression en fonction du degré polynomial du modèle")
# plt.show()


#### courbe apprentissage pour le meilleur polynôme ####


def courbe_apprentissage(X=X, Y=Y, iteration=150, degree_max=7):
    split = np.linspace(0.01, 0.95, num=iteration)
    r2 = np.zeros(int(split.shape[0]))
    for k in range(5, degree_max + 1):
        print(k)
        r2_k = []
        for s in split:
            x_tr, _, y_tr, _ = train_test_split(X, Y, train_size=s, random_state=0)
            x_, x, y_, y = train_test_split(x_tr, y_tr, random_state=0)
            pol = PolynomialFeatures(degree=k)
            x_train = pol.fit_transform(x_)
            x_test = pol.fit_transform(x)
            model = LinearRegression()
            model.fit(x_train, y_)
            pred_Y = model.predict(x_test)
            r2_k.append(r2_score(pred_Y,y ))
        r2 = np.vstack((r2, r2_k))
    return r2


courbe_apprentissage_score_regression= courbe_apprentissage()


plt.plot(np.linspace(0,X.shape[0],courbe_apprentissage_score_regression.shape[1]),courbe_apprentissage_score_regression[1],label = "Regression Polynomial de degré 5")
plt.plot(np.linspace(0,X.shape[0],courbe_apprentissage_score_regression.shape[1]),courbe_apprentissage_score_regression[2],label = "Regression Polynomial de degré 6")
plt.plot(np.linspace(0,X.shape[0],courbe_apprentissage_score_regression.shape[1]),courbe_apprentissage_score_regression[3],label = "Regression Polynomial de degré 7")


plt.xlabel("taille du dataset")
plt.ylabel("score de regression R2")
plt.title("Courbe d'apprentissage pour différents modèles polynomiaux")
plt.ylim(0,1)
plt.legend()
plt.show()
