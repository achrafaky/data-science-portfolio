import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement
iris_data = pd.read_csv("iris.csv", index_col="Id")

# DESSIN : Notez bien l'orthographe exacte avec les espaces et (cm)
plt.figure(figsize=(10, 6))
'''sns.histplot(data=iris_data, x='Petal Length (cm)', color='blue', alpha=0.5, kde=True, label='Petal Length (cm)')
sns.histplot(data=iris_data, x='Sepal Length (cm)', color='orange', alpha=0.5, kde=True, label='Sepal Length (cm)')
sns.histplot(data=iris_data, x='Petal Width (cm)', color='green', alpha=0.5, kde=True, label='Petal Width (cm)')
sns.histplot(data=iris_data, x='Sepal Width (cm)', color='red', alpha=0.5 , kde=True, label='Sepal Width (cm)')
plt.xlabel("Longueur et Largeur des Pétales et Sépales (cm)")

plt.title("Test A : Histogramme (Réussi !)")'''
'''sns.kdeplot(data=iris_data , x='Petal Length (cm)' , color='blue' , fill=True , alpha=0.5 , label='Petal Length (cm)')
sns.kdeplot(data=iris_data , x='Sepal Length (cm)' , color='orange' , fill=True , alpha=0.5 , label='Sepal Length (cm)')
sns.kdeplot(data=iris_data , x='Petal Width (cm)' , color='green' , fill=True , alpha=0.5 , label='Petal Width (cm)')
sns.kdeplot(data=iris_data , x='Sepal Width (cm)' , color='red' , fill=True , alpha=0.5 , label='Sepal Width (cm)')
'''
sns.jointplot(data=iris_data , x='Petal Length (cm)' , y='Petal Width (cm)' , hue='Species' , height=8)
sns.jointplot(data=iris_data , x='Sepal Length (cm)' , y='Sepal Width (cm)' , hue='Species' , height=8)
plt.figure(figsize=(12, 6))

# On compare la longueur des pétales par espèce
sns.boxplot(data=iris_data, x='Species', y='Petal Length (cm)')

plt.title("Box Plot : Le résumé statistique")
plt.show()
plt.show()