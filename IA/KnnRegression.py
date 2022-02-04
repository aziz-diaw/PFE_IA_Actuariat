import mglearn
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import GridSearchCV
import pandas
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

## Recupération de nos données
donnees = pandas.read_csv('combinaisons.csv',usecols=['age', 'nombre_payment' , 'maturite' , 'taux' , 'montant' ,'prime'])
#print(donnees)

## matrice de corrélation entre la prime et les facteurs explicatifs
correlation_matrix = donnees.corr()
u=correlation_matrix["prime"]
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
reg = KNeighborsRegressor(n_neighbors=1)
# fit the model using the training data and training targets
reg.fit(X_train, Y_train)
#print("Test set predictions:\n", reg.predict(X_test))
print("Test set R^2: {:.2f}".format(reg.score(X_test, Y_test)))

########## print de la target en fonction de chaque paramétre
"""""""""
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
"""""""""
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

