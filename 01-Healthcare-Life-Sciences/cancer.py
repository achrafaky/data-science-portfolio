# 1. Chargement des données
# On utilise index_col="Id" car l'ID du patient ne sert pas au calcul, c'est juste une étiquette.
from turtle import color
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cancer_filepath = "cancer.csv"
cancer_data = pd.read_csv(cancer_filepath, index_col="Id")

# 2. Inspection des mesures disponibles
plt.figure(figsize=(14, 6))

# Graphique de Gauche : Histogramme (La réalité brute)
'''plt.subplot(1, 2, 1)
sns.histplot(data=cancer_data, x='Area (mean)', hue='Diagnosis', element="step")
plt.title("Réalité Brute : Histogramme de la Surface")

# Graphique de Droite : KDE (La tendance lissée - Le plus important)
plt.subplot(1, 2, 2)
# fill=True colorie sous la courbe pour bien voir la zone
sns.kdeplot(data=cancer_data, x='Area (mean)', hue='Diagnosis', fill=True)
plt.title("Analyse de Densité : Distinction Bénin vs Malin")'''
'''sns.kdeplot(data=cancer_data, x='Smoothness (mean)', hue='Diagnosis', fill=True, alpha=0.5)
plt.title("Analyse de Densité : Distinction Bénin vs Malin")
plt.show()
sns.kdeplot(data=cancer_data, x='Concavity (mean)', hue='Diagnosis' , fill=True , alpha=0.5)
plt.title("Analyse de Densité : Distinction Bénin vs Malin")'''
'''sns.jointplot(data=cancer_data , x='Area (mean)' , y='Concavity (mean)' , hue='Diagnosis' , color='blue' , alpha=0.5 , height=8)
plt.figure(figsize=(12, 6))
sns.jointplot(data=cancer_data , x='Smoothness (mean)' , y='Concavity (mean)' , hue='Diagnosis' , color='red' , alpha=0.5 , height=8)
plt.title("Analyse conjointe : Surface vs Concavité")'''
# On sélectionne les 5 colonnes les plus intéressantes + le diagnostic
'''colonnes_a_tester = ['Area (mean)', 'Concavity (mean)', 'Texture (mean)', 'Smoothness (mean)', 'Radius (mean)', 'Diagnosis']

# La commande magique
sns.pairplot(data=cancer_data[colonnes_a_tester], hue='Diagnosis')
plt.show()
plt.show()'''
