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



#### Polynôme optimal ===> 5 ####
#
# def opti_poly_degree(degree_max):
#     r2 = []
#     for i in range(1, degree_max):
#         print("degrée : ", i)
#         pol = PolynomialFeatures(degree=i)
#         x_train = pol.fit_transform(X_train)
#         model = LinearRegression()
#         model.fit(x_train, Y_train)
#         pred_Y = model.predict(x_train)
#         r2.append(r2_score(Y_train, pred_Y))
#     return r2
#
#
# # degre_pol = opti_poly_degree(10)
# # print(degre_pol)
# # print("le modèle polynomial qui fit le mieux nos donnés est un modèle de degré : ", np.argmax(degre_pol)+1)
# # print("Le coeffcient r2 de ce modèle est : ", degre_pol[np.argmax(degre_pol)])








#### courbe apprentissage pour le meilleur polynôme ####

# def courbe_apprentissage(split = 2):
#
#     r2 = np.zeros(int(X_train.shape[0]/split))
#     for k in range(1,7):
#         print(k)
#         r2_k = []
#         for i in range(int(X_train.shape[0]/split)):
#         #for i in range(3) :
#             x = X_train[0:(split + split*i)]
#             y = Y_train.to_numpy()[0:(split +split*i)]
#             pol = PolynomialFeatures(degree=k)
#             x_train = pol.fit_transform(x)
#             model = LinearRegression()
#             model.fit(x_train, y)
#             pred_Y = model.predict(x_train)
#             r2_k.append(r2_score(y, pred_Y))
#         r2 = np.vstack((r2,r2_k))
#     return r2
#
#
# courbe_apprentissage_score_regression= courbe_apprentissage()
#
#
# split = 2
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[1],label = "Regression Polynomial de degré 1")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[2],label = "Regression Polynomial de degré 2")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[3],label = "Regression Polynomial de degré 3")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[4],label = "Regression Polynomial de degré 4")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[5],label = "Regression Polynomial de degré 5")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[6],label = "Regression Polynomial de degré 6")
# plt.xlabel("taille du dataset")
# plt.ylabel("score de regression R2")
# plt.title("Courbe d'apprentissage pour les dataset d'entrainements pour différents modèles polynomiaux")
# plt.legend()
# plt.show()



