import pandas
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

donnees = pandas.read_csv('combinaisons.csv',usecols=['age', 'nombre_payment' , 'maturite' , 'taux' , 'montant' ,'prime'])
Z = donnees.drop("prime", axis=1)
Y = Z.drop("age", axis=1)
X = Y
X = X.values
Y= donnees['prime']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)

model = LinearRegression().fit(X_train,Y_train)

print(X_test)
"""""""""
fig, axs = plt.subplots(1, 3)
axs[0, 0].scatter(x=X_test[:,0], y=model.predict(X_test))
axs[0,0].set(xlabel = 'age', ylabel= 'prime_prédite')

axs[0, 1].scatter(x=X_test[:,1], y=model.predict(X_test))
axs[0,1].set(xlabel = 'maturité', ylabel= 'prime_prédite')

axs[0, 2].scatter(x=X_test[:,2], y=model.predict(X_test))
axs[0,2].set(xlabel = 'montant', ylabel= 'prime_prédite')
"""""""""
#axs[0, 3].scatter(x=X_test[:,3], y=model.predict(X_test))
#axs[0,3].set(xlabel = 'taux', ylabel= 'prime_prédite')

#axs[2, 0].scatter(x=X_test[:,4], y=model.predict(X_test))
#axs[2,0].set(xlabel = 'montant', ylabel= 'prime_prédite')

plt.show()



r_sq = model.score(X, Y)
print('coefficient of determination:', r_sq)   ## R^2

print('intercept:', model.intercept_)      ## l'intercept

print('coeff:', model.coef_)  ## les coefficients

