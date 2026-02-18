# 1️⃣ Importer les bibliothèques
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pour que les graphiques s'affichent bien
sns.set(style="whitegrid")

# 2️⃣ Lire le fichier CSV
df = pd.read_csv("shopping.csv")  # Remplace par le chemin réel

# 3️⃣ Aperçu des données
print(df.head())
print(df.info())
print(df.describe())

# 4️⃣ Nettoyage de base
# Vérifier les valeurs manquantes
print(df.isnull().sum())

# Supprimer les colonnes inutiles pour certaines analyses (optionnel)
# df = df.drop(['Promo Code Used'], axis=1)

# 5️⃣ Analyse descriptive simple
print("Moyenne du montant des achats :", df['Purchase Amount (USD)'].mean())
print("Distribution par catégorie :")
print(df['Category'].value_counts())
print("Distribution par genre :")
print(df['Gender'].value_counts())

# 6️⃣ Visualisations

# Histogramme de l'âge
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=15, kde=True, color='skyblue')
plt.title("Distribution de l'âge des clients")
plt.xlabel("Âge")
plt.ylabel("Nombre de clients")
plt.show()

# Boxplot du montant par catégorie
plt.figure(figsize=(8,5))
sns.boxplot(x='Category', y='Purchase Amount (USD)', data=df, palette="Set2")
plt.title("Montant des achats par catégorie")
plt.show()

# Countplot des produits par saison
plt.figure(figsize=(10,5))
sns.countplot(x='Season', hue='Category', data=df, palette="coolwarm")
plt.title("Nombre de produits achetés par saison et catégorie")
plt.show()

# Scatterplot Montant vs Âge
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='Purchase Amount (USD)', hue='Category', data=df, palette="tab10")
plt.title("Montant des achats vs Âge")
plt.show()

# Heatmap des corrélations numériques
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.title("Corrélations entre les variables numériques")
plt.show()

