#Ceci est le script commun
import pandas as pd

url = "DataForTable2.1WHR2023.csv"

df = pd.read_csv(url)


import numpy as np


#fonctions d'affichage des graphes
import matplotlib.pyplot as plt
def graph(pays, indice):
    #on cherche d'abord les indices correspndant au pays 

    sub_df=df.loc[f"{pays}",[f"{indice}","year"]]             #on crée la dataframe qui nous intéresse seulement
    sub_df.plot()