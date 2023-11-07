# Objectif : L'indicateur du bonheur étudié ne prend pas en compte des phénomènes comme le suicide, nous allons étudier alors s'il existe un lien de corrélation entre suicide et bonheur tel que calculé précédemment pour voir si ceux-ci peuvent être liés, où si pour faire un modèle plus précis il est nécessaire de prendre en particulier les suicides. 

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
suicide = "Suicide_base.csv"
df1 = pd.read_csv(suicide)
##Importation de librairie usuelles"
##On note df le dataframe que nous utilisons ici

# L'idée est ici de voir si le bonheur est corrélé aux taux de suicide, pour cela on va s'aider d'une base de donnée ici du site : 
# https://www.kaggle.com/code/nickleejh/suicide-rates-1985-2020-tableau-visualisation/output
#
# Celle-ci répertorie les suicides pour différents pays entre 1985 et 2020 en fonction de divers caractéristiques notamment la tranche d'âge. 
#

df1.head(10)

# Cette base de donnée est très détaillée nous allons la travailler pour la simplifier un peu. Nous n'avons pour ce que l'on veut faire uniquement besoin d'une colonne pays, année, et taux de suicide total (c'est-à-dire qu'on ne classe pas par classe d'âge). 

df_sum=df1[['country','suicides_no','population','year']].groupby(['country','year']).sum()
df_sum['taux']=df_sum['suicides_no']/df_sum['population']
##On crée la base de donnée df_sum qui fait l'opération décrite précedemment et "simplifie" donc la base à notre usage. 

df_sum.head(10)

df_sum.tail(10)

# Remarquer que la base ici prend pour index à la fois 'country' et 'year' nous ne voulons que 'country' on fait faire un reset d'index 

df_sum=df_sum.reset_index()

df_sum.head()


# A partir de là on peut extraire les tables qui donnent pour un pays donnée ou pour une année donnée les taux de suicide et procéder à l'analyse des taux de corrélation. 
# Pour déterminer si les écarts sont importants on utilise les écarts quadratiques moyens. 

# +
def abs(x):
    if x >0 : 
        return x 
    else : 
        return -x

def ecart_quadra(x,y):
    return np.sqrt(abs(x**2-y**2))

##On définit ici les fonctions qui nous serons utile


# +
##On reprend le code du projet_happiness : 
url = "DataForTable2.1WHR2023.csv"
df = pd.read_csv(url)
df = df.ffill()
col = ['Log GDP per capita','Social support', 'Healthy life expectancy at birth',
       'Freedom to make life choices',
'Generosity','Perceptions of corruption']
for colonne in col :
    max = df[colonne].max()
    min = df[colonne].min()
    df[colonne] = (df[colonne]-min)/(max-min)
    df["big indice"] = 0
for colonne in col: 
    df["big indice"] = df["big indice"]+(df[colonne]/6)



# +
X=[i for i in range(2005,2021)] 

def corelation(pays):
    test1=df_sum['country'].isna()
    test2=df['Country name'].insa()
    if test1(pays) == True:
        return 'pas de données pour ce pays'
    else: 
    table=df_sum((df_sum['country']= pays) & (df_sum['year'] >= 2008) )
    L1=table['taux']
    table2=df(df['Country name'] = pays) & (df_sum['year'] <= 2020)) 
    L2=table['big indice']
    assert len(L1) == len(L2)
    L3= [ecart_quadra(x,y) for x,y in L1,L2] 
    plt.plot(X,L3) 

##Pour obtenir des données significatives on renormalise
