import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import GridSearchCV
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score

## Recupération de nos données
donnees = pandas.read_csv('combinaisons.csv',usecols=['age', 'nombre_payment' , 'maturite' , 'taux' , 'montant' ,'prime'])
#print(donnees)

## matrice de corrélation entre la prime et les facteurs explicatifs
# correlation_matrix = donnees.corr()
# u=correlation_matrix["prime"]
""""                             Corrélations : on voit que la variable la plus explicative est le montant
age               0.245662
nombre_payment   -0.214633
maturite          0.176561
taux             -0.049410
montant           0.313145
prime             1.000000
"""""
X = donnees.drop("prime", axis=1)
X = X.values
Y = donnees['prime']

########### split the wave dataset into a training and a test set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
# instantiate the model and set the number of neighbors to consider to 3
#reg = KNeighborsRegressor(n_neighbors=1)
# fit the model using the training data and training targets
#reg.fit(X_train, Y_train)
#print("Test set predictions:\n", reg.predict(X_test))
#print("Test set R^2: {:.2f}".format(reg.score(X_test, Y_test)))
#print("Train scrore: {:.2f}".format(reg.score(X_train, Y_train)))

########## print de la target en fonction de chaque paramétre
"""""""""""""""
plt.scatter(x=X_test[:,0], y=reg.predict(X_test))
plt.xlabel('age')
plt.ylabel('prime_prédite')
plt.show()

plt.scatter(x=X_test[:,1], y=reg.predict(X_test))
plt.xlabel('nombre_payment')
plt.ylabel('prime_prédite')
plt.show()

plt.scatter(x=X_test[:,2], y=reg.predict(X_test))
plt.xlabel('maturité')
plt.ylabel('prime_prédite')
plt.show()

plt.scatter(x=X_test[:,3], y=reg.predict(X_test))
plt.xlabel('taux')
plt.ylabel('prime_prédite')
plt.show()


plt.scatter(x=X_test[:,4], y=reg.predict(X_test))
plt.xlabel('montant')
plt.ylabel('prime_prédite')
plt.show()


fig, axs = plt.subplots(3, 2)
axs[0, 0].scatter(x=X_test[:,0], y=reg.predict(X_test))
axs[0,0].set(xlabel = 'age', ylabel= 'prime_prédite')

axs[0, 1].scatter(x=X_test[:,1], y=reg.predict(X_test))
axs[0,1].set(xlabel = 'nbre_payment', ylabel= 'prime_prédite')

axs[1, 0].scatter(x=X_test[:,2], y=reg.predict(X_test))
axs[1,0].set(xlabel = 'maturité', ylabel= 'prime_prédite')

axs[1, 1].scatter(x=X_test[:,3], y=reg.predict(X_test))
axs[1,1].set(xlabel = 'taux', ylabel= 'prime_prédite')

axs[2, 0].scatter(x=X_test[:,4], y=reg.predict(X_test))
axs[2,0].set(xlabel = 'montant', ylabel= 'prime_prédite')

plt.show()


fig1, axs = plt.subplots(3, 2)
axs[0, 0].scatter(x=X_train[:,0], y=Y_train)
axs[0,0].set(xlabel = 'age', ylabel= 'prime_entrainement')

axs[0, 1].scatter(x=X_train[:,1], y=Y_train)
axs[0,1].set(xlabel = 'nbre_payment', ylabel= 'prime_entrainement')

axs[1, 0].scatter(x=X_train[:,2], y=Y_train)
axs[1,0].set(xlabel = 'maturité', ylabel= 'prime_entrainement')

axs[1, 1].scatter(x=X_train[:,3], y=Y_train)
axs[1,1].set(xlabel = 'taux', ylabel= 'prime_entrainement')

axs[2, 0].scatter(x=X_train[:,4], y=Y_train)
axs[2,0].set(xlabel = 'montant', ylabel= 'prime_entrainement')


plt.show()

"""""""""""


############## Détermination du meilleur K


parameters = {"n_neighbors": range(1, 50)}
gridsearch = GridSearchCV(KNeighborsRegressor(), parameters)
gridsearch.fit(X_train, Y_train)
print(gridsearch.best_params_)


"""""""""

#Analyze k-neighbors regression
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for n_neighbors, ax in zip([1, 3, 9], axes):
    # make predictions using 1, 3, or 9 neighbors
    reg = KNeighborsRegressor(n_neighbors=n_neighbors)
    reg.fit(X_train, Y_train) ## on entraine
    ax.plot(X_train, Y_train, '^', c=mglearn.cm2(0), markersize=8)
    ax.plot(X_test, Y_test, 'v', c=mglearn.cm2(1), markersize=8)

    ax.set_title(
        "{} neighbor(s)\n train score: {:.2f} test score: {:.2f}".format(
            n_neighbors, reg.score(X_train, Y_train),
            reg.score(X_test, Y_test)))    ## A chaque fois on affichera le train score et le test score
    ax.set_xlabel("Features")
    ax.set_ylabel("Target")
axes[0].legend(["Model predictions", "Training data/target",
                "Test data/target"], loc="best")
plt.show()
"""""""""


#### plot de la précision en fonction de k

# training_accuracy = []
# test_accuracy = []
# # try n_neighbors from 1 to 50
# neighbors_settings = range(1, 51)
#
# for n_neighbors in neighbors_settings:
#     # build the model
#     clf = KNeighborsRegressor(n_neighbors=n_neighbors)
#     clf.fit(X_train, Y_train)
#     # record training set accuracy
#     training_accuracy.append(clf.score(X_train, Y_train))
#     # record generalization accuracy
#     test_accuracy.append(clf.score(X_test, Y_test))
#
# plt.plot(neighbors_settings, training_accuracy, label="Précision donnnées d'entrainement")
# plt.plot(neighbors_settings, test_accuracy, label="Précision données de test")
# plt.ylabel("Score de précision")
# plt.xlabel("Nombre de voisins")
# plt.title("Visualisation du score de précision en fonction du nombre de voisin ")
# plt.legend()
# plt.show()

#### courbe apprentissage pour le meilleur polynôme ####

def courbe_apprentissage(split = 2):

    r2 = np.zeros(int(X.shape[0]/split))
    for k in range(1,3):
        r2_k = []
        for i in range(int(X.shape[0]/split)):
            x_train=X_train[0:(split + split*i)]
            y_train=Y_train[0:(split + split*i)]
            x_test = X_test[0:(split + split*i)]
            y_test = Y_test.to_numpy()[0:(split +split*i)]
            model = KNeighborsRegressor(n_neighbors=k)
            model.fit(x_train, y_train)
            pred_Y = model.predict(x_test)
            r2_k.append(r2_score(y_test, pred_Y))

        r2 = np.vstack((r2,r2_k))
    return r2


courbe_apprentissage_score_regression= courbe_apprentissage()
print(courbe_apprentissage_score_regression[1])
#
#
split = 2
plt.plot(range(0,3150,2),courbe_apprentissage_score_regression[1],label = "Regression knn pour k=1")
#plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[2],label = "Regression knn pour k=2")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[3],label = "Regression Polynomial de degré 3")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[4],label = "Regression Polynomial de degré 4")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[5],label = "Regression Polynomial de degré 5")
# plt.plot(range(split,X_train.shape[0]+split,split),courbe_apprentissage_score_regression[6],label = "Regression Polynomial de degré 6")

# plt.plot(range(split,X_test.shape[0]+split,split),courbe_apprentissage_score_regression[1],label = "Regression Polynomial de degré 1")
# plt.plot(range(split,X_test.shape[0]+split,split),courbe_apprentissage_score_regression[2],label = "Regression Polynomial de degré 2")
# plt.plot(range(split,X_test.shape[0]+split,split),courbe_apprentissage_score_regression[3],label = "Regression Polynomial de degré 3")
# plt.plot(range(split,X_test.shape[0]+split,split),courbe_apprentissage_score_regression[4],label = "Regression Polynomial de degré 4")
# plt.plot(range(split,X_test.shape[0]+split,split),courbe_apprentissage_score_regression[5],label = "Regression Polynomial de degré 5")
# plt.plot(range(split,X_test.shape[0]+split,split),courbe_apprentissage_score_regression[6],label = "Regression Polynomial de degré 6")
# plt.xlabel("taille du dataset")
# plt.ylabel("score de regression R2")
# plt.title("Courbe d'apprentissage pour les dataset de test pour différents modèles polynomiaux")
# plt.legend()
plt.show()