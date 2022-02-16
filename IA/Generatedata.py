################################################        Génération du set de paramétre                   ###########################################
import pandas
import numpy as np
import Actuariat.probabilities_one_insured as poi
import Table.tables as table
from matplotlib import pyplot as plt
import Actuariat.commutation_case_death as ccd
import Actuariat.commutation_case_life as ccl
import Actuariat.insurance_case_death as icd
import Actuariat.life_annuities as lan
import Actuariat.product as prod
import seaborn as sns
import pandas as pd
pd.options.mode.chained_assignment = None
from numpy import random

"""""""""""
## Génération préalable des données de maniére aléatoire et enregistrement sur un CSV

## Vu qu'on est contraint par (m<n), je vais construire les combinaisons possible pour chaque maturié avant de les joindres

### Pour tous les ages sans qu'il n'y est d'anomalies :
prime=[]
liste=[]
for i in range (0,10000):
    payment1 = random.choice([1])
    payment2 = random.choice([1, 5])
    payment3 = random.choice([1, 5, 10])
    payment4 = random.choice([1, 5, 10 ,20])
    payment5 = random.choice([1, 5, 10, 20, 30])
    payment6 = random.choice([1, 5, 10, 20, 30, 40])
    age = random.choice([20, 30, 40, 50, 60])
    taux= random.choice([0, 0.005, 0.01, 0.015, 0.02, 0.025])
    montant = random.choice([500, 1000, 2000, 4000, 8000])
    liste1=[]
    liste2=[]
    liste3=[]
    liste4=[]
    liste5=[]
    liste6=[]


    liste1 += [ age,payment1,1, taux,montant]
    liste2 += [age, payment2, 5, taux, montant]
    liste3 += [age, payment3,10 , taux , montant]
    liste4 += [age, payment4, 20, taux, montant]
    liste5 += [age, payment5, 30, taux, montant]
    liste6 += [age, payment6, 40, taux, montant]

    liste +=[liste1] + [liste2]+ [liste3] + [liste4]+ [liste5] + [liste6]

################ Création de la dataframe
columns = ['age','nombre_payment','maturite', 'taux', 'montant']
df = pd.DataFrame(data=liste,columns=columns)

############################## suppression des doublons
df2=df.drop_duplicates()

print(df2.shape)
#print(df2)

##################################### Calcul de la prime et rajout dans le dataframe
## calcul prime_annuelle
def calculprime(i):
    return (prod.nAx(df2['age'].iloc[i],df2['maturite'].iloc[i],df2['taux'].iloc[i], table.TH_00_02)*df2['montant'].iloc[i])/lan._a_xn_(df2['age'].iloc[i],df2['nombre_payment'].iloc[i],df2['taux'].iloc[i],table.TD_88_90)



for i in range(len(df2)):
    #print(df2['age'].iloc[i])
    prime= prime + [calculprime(i)]
#print(prime)
 ####rajout dans le dataframe

df2['prime'] = prime
print(df2)
df2.to_csv('combinaisons.csv')

#print (df2)
"""""""""""

############################################################### Analyse de données sur recupération du fichier CSV ###########################################################"


donnees = pandas.read_csv('combinaisons.csv',usecols=['age', 'nombre_payment' , 'maturite' , 'taux' , 'montant' ,'prime'])

"""""""""
plt.scatter(donnees['age'],donnees['prime'])

plt.title('Prime en fonction de l\'age')
plt.xlabel('age')
plt.ylabel('prime')
plt.show()
"""""""""
"""""
count  3150.000000     3150.000000  ...  3150.000000  3150.000000
mean     40.000000       11.000000  ...  3100.000000   223.660570
std      14.144381       11.107317  ...  2728.069401   628.547859
min      20.000000        1.000000  ...   500.000000     0.694900
25%      30.000000        1.000000  ...  1000.000000    12.993785
50%      40.000000        5.000000  ...  2000.000000    43.683357
75%      50.000000       20.000000  ...  4000.000000   161.432473
max      60.000000       40.000000  ...  8000.000000  7974.305115
"""""

###  Faire l'analyse de donnée en phrase et essayer de tracer le nuage de point plus parlant qu'un boxplot


##### Ensemble des boxplots
# data_1 = donnees['age']
# data_2 = donnees['montant']
# data_3 = donnees['nombre_payment']
data_4 = donnees['prime']
# data_5 = donnees['taux']
# data_6 = donnees['maturite']
# data = [data_1, data_2, data_3, data_4, data_5, data_6]

# fig = plt.figure(figsize=(10, 7))
# ax = fig.add_axes([0, 0, 1, 1])
# ax.set(xlabel = 'age', ylabel= 'prime')
# bp = ax.boxplot(data)
# plt.show()

fig1, ax1 = plt.subplots()
ax1.set_title('Boxplot des Primes')
ax1.boxplot(data_4)
plt.xlabel("primes")
plt.ylabel("valeurs en € ")
plt.show()

#### comportement de la prime en fonction de chaque paramétre



donnees = pandas.read_csv('combinaisons.csv',usecols=['age', 'nombre_payment' , 'maturite' , 'taux' , 'montant' ,'prime'])
fig, axs = plt.subplots(3, 2)
axs[0, 0].scatter(x=donnees['age'], y=donnees['prime'])
axs[0,0].set(xlabel = 'age', ylabel= 'prime')

axs[0, 1].scatter(x=donnees['nombre_payment'], y=donnees['prime'])
axs[0,1].set(xlabel = 'nbre_payment', ylabel= 'prime_prédite')

axs[1, 0].scatter(x=donnees['maturite'], y=donnees['prime'])
axs[1,0].set(xlabel = 'maturité', ylabel= 'prime_prédite')

axs[1, 1].scatter(x=donnees['taux'], y=donnees['prime'])
axs[1,1].set(xlabel = 'taux', ylabel= 'prime_prédite')

axs[2, 0].scatter(x=donnees['montant'], y=donnees['prime'])
axs[2,0].set(xlabel = 'montant', ylabel= 'prime_prédite')

plt.show()


# sns.boxplot(data= donnees, y = "prime", x = "maturite")  #### évolution prime en fonction de la maturité
# plt.show()
#
#
# sns.boxplot(data= donnees, y = "prime", x = "age")  #### évolution prime en fonction de l'age
# plt.show()
#
#
# sns.boxplot(data= donnees, y = "prime", x = "nombre_payment")  #### évolution prime en fonction du nombre de payment
# plt.show()
#
#
# sns.boxplot(data= donnees, y = "prime", x = "taux")  #### évolution prime en fonction du taux
# plt.show()







