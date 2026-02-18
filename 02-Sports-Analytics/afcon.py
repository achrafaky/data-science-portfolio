import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np  # Indispensable pour np.select

# --- 1. PRÉPARATION DES DONNÉES ---
try:
    print("⏳ Chargement des données...")
    df = pd.read_csv("afcon.csv", on_bad_lines='skip')
    
    # Nettoyage et création des colonnes de buts
    if 'Score (Team1 - Team2)' in df.columns:
        # On divise le score "2 - 1" en deux chiffres
        split_data = df['Score (Team1 - Team2)'].str.split(' - ', expand=True)
        df['Goals_Team1'] = pd.to_numeric(split_data[0])
        df['Goals_Team2'] = pd.to_numeric(split_data[1])
        
        # --- CLASSIFICATION DES MATCHS (La correction est ici 👇) ---
        conditions = [
            (df['Goals_Team1'] > df['Goals_Team2']), # Victoire
            (df['Goals_Team1'] < df['Goals_Team2']), # Défaite
            (df['Goals_Team1'] == df['Goals_Team2']) # Nul
        ]
        choices = ['Victoire', 'Défaite', 'Nul']
        
        # AJOUT DE default='Indéfini' pour éviter l'erreur de type
        df['Resultat_Match'] = np.select(conditions, choices, default='Indéfini')
        
        print("✅ Données classées avec succès (Victoire/Défaite/Nul) !")

        # --- 2. VISUALISATION EXPERT ---
        sns.set_theme(style="whitegrid")

        # Graphique A : Régression Visuelle (Tendance)
        # Montre si la possession aide à marquer
        print("📊 Génération du graphique de tendance...")
        sns.lmplot(data=df, x='Team 1 Possession percentage', y='Goals_Team1', 
                   hue='Resultat_Match', height=7, aspect=1.5,
                   palette={'Victoire': 'green', 'Défaite': 'red', 'Nul': 'gray', 'Indéfini': 'black'})
        
        plt.title("Impact de la Possession sur les Buts (Lignes de tendance)")
        plt.xlabel("Possession (%)")
        plt.ylabel("Buts Marqués")
        plt.show()

        # Graphique B : Comparaison Directe (Boxplot)
        # Montre la distribution de la possession pour les gagnants vs perdants
        print("📊 Génération du comparatif...")
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='Resultat_Match', y='Team 1 Possession percentage', 
                    order=['Victoire', 'Nul', 'Défaite'],
                    palette={'Victoire': 'green', 'Défaite': 'red', 'Nul': 'gray'})
        
        plt.title("Les gagnants ont-ils vraiment plus le ballon ?")
        plt.ylabel("Possession de balle (%)")
        plt.show()

    else:
        print("⚠️ La colonne 'Score (Team1 - Team2)' est introuvable.")

except Exception as e:
    print(f"❌ Une erreur est survenue : {e}")'''
'''import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re # Module pour chercher du texte (Regex)

# --- 1. CHARGEMENT ---
try:
    print("⏳ Chargement et extraction des buteurs...")
    df = pd.read_csv("afcon.csv", on_bad_lines='skip')

    # Liste pour stocker chaque but individuel : [Nom du Joueur, Contre qui il a marqué]
    goals_data = []

    # Fonction pour nettoyer le texte (ex: "Salah - 55'"  -> "Salah")
    def extraire_buteurs(texte_buteurs, equipe_adverse):
        if pd.isna(texte_buteurs):
            return
        
        # On cherche le motif : "Nom du joueur" suivi de " - " et d'un chiffre
        # Ce regex capture tout ce qui est avant le tiret des minutes
        buteurs = re.findall(r"([a-zA-ZÀ-ÿ\s\.-]+)(?: - \d+)", str(texte_buteurs))
        
        for joueur in buteurs:
            joueur_clean = joueur.strip() # Enlève les espaces inutiles
            if len(joueur_clean) > 2: # Sécurité pour éviter les erreurs vides
                goals_data.append({'Joueur': joueur_clean, 'Contre_Equipe': equipe_adverse})

    # --- 2. BOUCLE SUR TOUS LES MATCHS ---
    for index, row in df.iterrows():
        # On extrait les buteurs de l'équipe 1 (ils ont marqué contre Team2)
        extraire_buteurs(row['Goal Scorers Team 1'], row['Team2'])
        
        # On extrait les buteurs de l'équipe 2 (ils ont marqué contre Team1)
        extraire_buteurs(row['Goal Scorers Team 2'], row['Team1'])

    # On transforme la liste en un vrai Tableau de Données (DataFrame)
    df_goals = pd.DataFrame(goals_data)

    print(f"✅ Extraction réussie ! {len(df_goals)} buts analysés.")
    
    # --- 3. PRÉPARATION DE LA HEATMAP ---
    # On compte combien de buts chaque joueur a mis contre chaque équipe
    # On ne garde que les joueurs qui ont mis au moins 2 buts au total (pour alléger le graphique)
    
    top_players = df_goals['Joueur'].value_counts()
    top_scorers_list = top_players[top_players >= 2].index # Garde les joueurs avec 2+ buts
    
    # On filtre les données pour ne garder que ces 'Top Scorers'
    df_top = df_goals[df_goals['Joueur'].isin(top_scorers_list)]

    # CRÉATION DE LA MATRICE (Pivot Table) pour la Heatmap
    # Lignes = Joueurs, Colonnes = Équipes Adverses, Valeurs = Nombre de buts
    heatmap_data = pd.crosstab(df_top['Joueur'], df_top['Contre_Equipe'])

    print("📊 Génération de la Heatmap des Buteurs...")

    # --- 4. VISUALISATION (HEATMAP) ---
    plt.figure(figsize=(12, 10))
    
    # cmap="YlOrRd" = Jaune (peu de buts) -> Rouge (beaucoup de buts)
    sns.heatmap(heatmap_data, annot=True, cmap="YlOrRd", linewidths=.5)
    
    plt.title("HEATMAP : Qui sont les dangers publics ?\n(Joueurs vs Équipes Adverses)", fontsize=16)
    plt.xlabel("Adversaire")
    plt.ylabel("Buteur")
    plt.yticks(rotation=0) # Garde les noms à l'horizontale
    plt.show()

    # Petit bonus textuel dans le terminal
    print("\n🏆 TOP 5 DES MEILLEURS BUTEURS (RATING) :")
    print(top_players.head(5))

except Exception as e:
    print(f"❌ Erreur : {e}")'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. PRÉPARATION AVANCÉE DES DONNÉES ---
try:
    print("⏳ Préparation des données pour le Jointplot...")
    df = pd.read_csv("afcon.csv", on_bad_lines='skip')

    # On nettoie les scores comme d'habitude
    if 'Score (Team1 - Team2)' in df.columns:
        split_data = df['Score (Team1 - Team2)'].str.split(' - ', expand=True)
        df['Goals_Team1'] = pd.to_numeric(split_data[0])
        df['Goals_Team2'] = pd.to_numeric(split_data[1])

        # --- L'ASTUCE DATA SCIENCE (Melt / Concat) ---
        # Pour faire un beau jointplot, on veut que chaque ligne soit une "Performance d'équipe"
        # On crée une liste pour l'Équipe 1
        team1_stats = df[['Team 1 Possession percentage', 'Goals_Team1']].copy()
        team1_stats.columns = ['Possession', 'Buts'] # On renomme pour que ce soit pareil
        
        # On crée une liste pour l'Équipe 2
        team2_stats = df[['Team 2 Possession percentage', 'Goals_Team2']].copy()
        team2_stats.columns = ['Possession', 'Buts'] # On renomme pareil

        # On colle les deux l'un sous l'autre (Concaténation)
        # Maintenant, on a 2x plus de données à analyser !
        df_final = pd.concat([team1_stats, team2_stats])

        print(f"✅ Données fusionnées ! {len(df_final)} performances d'équipes prêtes à être analysées.")

        # --- 2. VISUALISATION (JOINTPLOT) ---
        sns.set_theme(style="darkgrid")
        
        # kind='reg' ajoute une ligne de régression et une ombre de densité
        # C'est le top pour voir la distribution ET la corrélation
        g = sns.jointplot(data=df_final, x='Possession', y='Buts', 
                          kind='reg', 
                          color='purple',
                          height=8,
                          space=0)

        # Personnalisation des titres
        g.fig.suptitle("Distribution : Possession vs Efficacité des Buteurs", y=1.02, fontsize=16)
        g.set_axis_labels("Possession de Balle (%)", "Nombre de Buts Marqués", fontsize=12)
        
        plt.show()
        
    else:
        print("⚠️ Colonne Score introuvable.")

except Exception as e:
    print(f"❌ Erreur : {e}")