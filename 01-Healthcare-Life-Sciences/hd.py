import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- 1. PRÉPARATION DES DONNÉES ---
try:
    print("🔥 Calcul des corrélations en cours...")
    df = pd.read_csv("Heart_Disease_Prediction.csv")

    # ÉTAPE CRITIQUE : La machine ne comprend pas "Presence/Absence".
    # On doit transformer le diagnostic en chiffres (1 et 0) pour que la corrélation fonctionne.
    # Si on ne fait pas ça, la ligne "Heart Disease" n'apparaîtra pas !
    df['Heart Disease'] = df['Heart Disease'].map({'Presence': 1, 'Absence': 0})

    # --- 2. CRÉATION DE LA MATRICE DE CORRÉLATION ---
    # On ne garde que les colonnes numériques
    corr_matrix = df.select_dtypes(include=['float64', 'int64']).corr()

    # --- 3. LE DESIGN "EXPERT" (Le Masque) ---
    # Création d'un masque pour cacher la moitié haute du triangle (redondante)
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

    # Configuration de la taille
    plt.figure(figsize=(14, 10))

    # --- 4. LE DESSIN ---
    # cmap='coolwarm' : Rouge = Forte corrélation positive (Danger)
    #                   Bleu  = Forte corrélation négative (Protection)
   ''' heatmap = sns.heatmap(corr_matrix, 
                          mask=mask, 
                          annot=True,      # Affiche les chiffres
                          fmt=".2f",       # 2 chiffres après la virgule
                          cmap='coolwarm', # Couleurs Chaud/Froid
                          linewidths=0.5,  # Lignes blanches entre les cases
                          cbar_kws={"shrink": .8}) # Barre de légende ajustée

    plt.title("🔥 Carte Globale des Facteurs de Risque Cardiaque", fontsize=18)
    plt.xticks(rotation=45, ha='right') # Rotation des noms pour lisibilité
    plt.show()'''
sns.jointplot(data=df, x='Depression_ST', y='Slope', hue='Heart Disease', color='blue', height=8)
plt.title("Analyse conjointe : Dépression ST vs Slope")
plt.show()
except Exception as e:
    print(f"❌ Erreur : {e}")