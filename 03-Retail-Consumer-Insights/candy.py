import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Chargement avec la colonne ID pour avoir les noms des bonbons
candy_data = pd.read_csv("03-Retail-Consumer_Insights/candy.csv", index_col="id")

# 2. Configuration de la taille
plt.figure(figsize=(10,6))

# 3. Le Scatter Plot (Ta syntaxe est maintenant correcte ici)
sns.scatterplot(data=candy_data, x="sugarpercent", y="winpercent", hue="chocolate", palette="Set1", s=100, alpha=0.7)

# 4. Titres et affichage
plt.title("Relation entre le pourcentage de sucre et le pourcentage de gagnants")
plt.xlabel("Pourcentage de sucre")
plt.ylabel("Pourcentage de gagnants")

# Note : lmplot gère sa propre fenêtre, pas besoin de plt.figure() avant
sns.lmplot(data=candy_data, x="sugarpercent", y="winpercent", hue="chocolate")

plt.title("Comparaison des pentes : Chocolat vs Pas Chocolat")
plt.show()
sns.swarmplot(data=candy_data, x="chocolate", y="winpercent", palette="Set2")
plt.title("Distribution du pourcentage de gagnants selon le chocolat")
plt.show()
