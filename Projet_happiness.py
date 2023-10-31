#Ceci est le script commun
import pandas as pd

url = "DataForTable2.1WHR2023.csv"

df = pd.read_csv(url)
#par soucis de remplissage des cases pour calculer l'indice de bonheur, en remplie les cases vides par les cases précedentes (pas de cases vides en première année)
df = df.ffill() 
df.head()


# + active=""
# Le poids accorder à chacun de ces colonnes est subjectif, On part donc dans un premier temps que chaque colonne doit avoir le même poids que les autres. On va assimiler chaque données numériques à un nombre entre 0 et 1 de sorte que le pire pays soit à 0 et le meilleur à 1 (attention il y a encore une part de subjectif étant donné qu'on a par exemple le log du PIB/hab comme données). Aussi, d'après leur document, les 6 facteurs suivant ressortent : GDP per capita, social support, life expectancy, freedom to make choice, generosity, perception of corruption.  
# -

col = ['Log GDP per capita','Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices',
'Generosity','Perceptions of corruption']
for colonne in col :
    max = df[colonne].max()
    min = df[colonne].min()
    df[colonne] = (df[colonne]-min)/(max-min)
df.head()

df.head()

# +
df["big indice"] = 0
for colonne in col: 
    df["big indice"] = df["big indice"]+(df[colonne]/6)
    
df.head()
# -


import numpy as np

##fonctions d'affichage des graphes

#pour plusieurs indices d'un pays
import matplotlib.pyplot as plt
def graphindice(pays, indice, *autres_indices):
    masque=df['Country name']==pays
    sub_df=df[[indice, *autres_indices , "year",'Country name']]         #on crée la dataframe qui nous intéresse
    sub_df[masque].plot(x="year")
    plt.show()

graphindice("Albania","Social support", "Perceptions of corruption","Freedom to make life choices")

#pour plusieurs pays mais 1 indice
def graphpays(indice, p1, *autres_pays):
    sub_df=df[[indice, "year",'Country name']]         #on crée la dataframe qui nous intéresse
    sub_df=sub_df.T
    sub_df[p1, *autres_pays].plot(x="year")
    plt.show()

#graphpays("Social support","Albania","Afghanistan")

#histogramme de la répartition du big indice
def histbi(année):
    masque=df['year']==année
    sub_df=df[["big indice", "year",'Country name']]         #on crée la dataframe qui nous intéresse
    sub_df[masque].hist(x="big indice")
    plt.show()

histbi(2000)
