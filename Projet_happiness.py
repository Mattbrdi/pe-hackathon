#Ceci est le script commun
import pandas as pd

url = "DataForTable2.1WHR2023.csv"

df = pd.read_csv(url)


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
def graphpays(indice, p1, p2):
    masque=(df['Country name']==p1) | (df['Country name']==p2)
    sub_df=df[[indice, "year",'Country name']]         #on crée la dataframe qui nous intéresse
    sub_df[masque].plot(x="year")
    plt.show()

graphpays("Social support","Albania","Afghanistan")

#histogramme de la répartition du big indice
def histbi(année):
    masque=df['year']==année
    sub_df=df[["big indice", "year",'Country name']]         #on crée la dataframe qui nous intéresse
    sub_df[masque].hist(x="big indice")
    plt.show()

histbi(2000)
