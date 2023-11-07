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

##L'algorithme qui suit vise à tracer pour un pays donné et sur la période 2008 2020 
##l'évolution des écarts quadratique moyens entre indice de bonheur global et taux de suicide. 
##L'existence d'ne faible pente d'évolution (voire d'une constante) traduit l'existance d'une corrélation
##S'il n'y a pas de pente ou que celle-ci est sensiblement pentu, c'est qu'au moins dans ce pays suicides et 
##bonheur ne sont pas corrélés 
def corelation(pays):
    country_count1=df_sum['country'].str.contains(pays).sum()
    country_count2=df['Country name'].str.contains(pays).sum()
    if country_count1 ==0:
        return 'pas de données pour ce pays'
    if country_count2 ==0:
        return 'pas de données pour ce pays'
    ##Vérifications pour s'assurer que l'on possède les données nécessaires dans les deux tables
    else: 
    table=df_sum((df_sum['country']= pays) & (df_sum['year'] >= 2008) )
    L1=table['taux']
    ##C'est la table des taux de suicide pour le pays donné entre les années 2008 et 2020 pour 
    ##être compatible avec l'autre table
    table2=df(df['Country name'] = pays) & (df_sum['year'] <= 2020)) 
    L2=table['big indice']
    ##C'est la table du big indice sur la même période, notons que les data frame sont rangés par 
    ##date croissante et que grâce à ça l'on a s'évite des étable de traitement de donnée suplémentaires
    assert len(L1) == len(L2)
    ##dernière vérification de compatibilité
    L3= [ecart_quadra(x,y) for x,y in L1,L2] 
    plt.plot(X,L3) 
    plt.show() 