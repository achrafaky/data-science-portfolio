import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuration du style
sns.set_theme(style="darkgrid")

# Chemin intelligent pour fifa.csv (cherche dans le dossier ou à côté)
if os.path.exists("02-Sports-Analytics/fifa.csv"):
    file_path = "02-Sports-Analytics/fifa.csv"
else:
    file_path = "fifa.csv"

if os.path.exists(file_path):
    print(f"⏳ Chargement des données depuis : {file_path} ...")
    fifa_data = pd.read_csv(file_path, index_col="Date", parse_dates=True)
    print("✅ Fichier chargé avec succès !")
    
    # -------------------------------------------------------
    # EXERCICE : COMPARER ARGENTINE vs BRÉSIL
    # -------------------------------------------------------
    plt.figure(figsize=(16, 6))

    # Sélection des équipes et tracé des lignes
    columns_to_plot = ['ARG', 'BRA'] 
    sns.lineplot(data=fifa_data[columns_to_plot], linewidth=2.5)
    
    # Titres et légendes du graphique
    plt.title("Comparaison : Argentine (ARG) vs Brésil (BRA)", fontsize=16)
    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Classement FIFA (Plus bas = Meilleur)", fontsize=12)
    
    # Affichage du graphique
    plt.show()

else:
    print(f"❌ Erreur : Impossible de trouver le fichier CSV.")