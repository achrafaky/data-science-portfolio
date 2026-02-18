import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration esthétique
sns.set(style="whitegrid")
# Charger les données
df = pd.read_csv("shopping.csv")
'''import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df = pd.read_csv("shopping.csv")

# Line chart : Montant des achats par Customer ID
plt.figure(figsize=(12,5))
plt.plot(df['Customer ID'], df['Purchase Amount (USD)'], marker='o')
plt.title("Montant des achats par Customer ID")
plt.xlabel("Customer ID")
plt.ylabel("Purchase Amount (USD)")
plt.grid(True)
plt.show()

# Line chart : Age par Customer ID
plt.figure(figsize=(12,5))
plt.plot(df['Customer ID'], df['Age'], marker='o', color='orange')
plt.title("Âge des clients par Customer ID")
plt.xlabel("Customer ID")
plt.ylabel("Age")
plt.grid(True)
plt.show()'''
# Bar chart : Nombre de clients par Category
'''plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Category', palette="Set2")
plt.title("Nombre de clients par Category")
plt.show()

# Bar chart : Nombre de clients par Gender
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Gender', palette="Set1")
plt.title("Nombre de clients par Gender")
plt.show()

# Bar chart : Montant moyen d'achat par Category
plt.figure(figsize=(10,5))
sns.barplot(data=df, x='Category', y='Purchase Amount (USD)', palette="Set3")
plt.title("Montant moyen d'achat par Category")
plt.show()'''
# Corrélations numériques
'''numerical_cols = ['Age', 'Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']
plt.figure(figsize=(10,6))
sns.heatmap(data=df, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Corrélations entre variables numériques")
plt.show()'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset
df = pd.read_csv("shopping.csv")

# Encoder toutes les colonnes non numériques
df_encoded = df.copy()
for col in df_encoded.columns:
    if df_encoded[col].dtype == 'object':
        df_encoded[col] = pd.factorize(df_encoded[col])[0]

# Heatmap pour toutes les colonnes
plt.figure(figsize=(15,12))
sns.heatmap(df_encoded.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Heatmap des corrélations pour toutes les colonnes (numériques + catégorielles encodées)", fontsize=14)
plt.show()