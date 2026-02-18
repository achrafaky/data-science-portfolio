import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import os

# 1. Chargement des données
# On s'assure que la colonne Platform devient l'index (les étiquettes des lignes)
# Chemin dynamique adaptatif (Idéal pour les environnements Git/Kaggle/Locaux)
if os.path.exists("03-Retail-Consumer-Insights/ign_scores.csv"):
    file_path = "03-Retail-Consumer-Insights/ign_scores.csv"
else:
    file_path = "ign_scores.csv"

if os.path.exists(file_path):
    print(f"⏳ Chargement des données depuis : {file_path} ...")
    # Configuration de la colonne 'Platform' comme index du DataFrame
    ign_data = pd.read_csv(file_path, index_col="Platform")
    print("✅ Fichier chargé avec succès !")

# --- GRAPHIQUE 1 : LE BAR CHART (Horizontal pour la lisibilité) ---
plt.figure(figsize=(12, 10)) # On fait une grande image
plt.title("Meilleure plateforme pour les jeux de Course (Racing)")

# Astuce d'expert : On met les Plateformes sur l'axe Y (vertical)
# pour que les noms soient écrits à l'horizontale et lisibles.
sns.barplot(x=ign_data['Racing'], y=ign_data.index)

plt.xlabel("Score Moyen")
plt.show()

# --- GRAPHIQUE 2 : LA HEATMAP (Vue d'ensemble) ---
plt.figure(figsize=(14, 10)) # Très grand pour voir tous les chiffres
plt.title("Carte de chaleur : Tous les genres sur toutes les consoles")

# On utilise une couleur (cmap) 'YlGnBu' (Jaune-Vert-Bleu) qui est très lisible
# Plus c'est foncé, meilleur est le score.
sns.heatmap(data=ign_data, annot=True, cmap="YlGnBu")

plt.xlabel("Genre de Jeu")
plt.show()