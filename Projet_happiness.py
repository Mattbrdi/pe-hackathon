#Ceci est le script commun
import pandas as pd

url = "DataForTable2.1WHR2023.csv"

df = pd.read_csv(url)


import numpy as np

#fonctions d'affichage des graphes
import matplotlib.pyplot as plt
def graph(pays, indice, *autres_indices):
    masque=df['Country name']==pays
    sub_df=df[[indice, *autres_indices , "year",'Country name']]         #on crée la dataframe qui nous intéresse
    sub_df[masque].plot(x="year")
    plt.show()

graph("Albania","Social support", "Perceptions of corruption","Freedom to make life choices")