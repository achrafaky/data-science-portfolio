import pandas as pd
import chardet

# Remplace par le nom EXACT de ton fichier téléchargé
filename = "ks-projects-201801-utf8.csv"

# --- ÉTAPE 1 : Le Détective ---
# On lit les 100 000 premiers octets pour deviner l'encodage
print("🕵️‍♂️  Analyse de l'encodage en cours...")
with open(filename, 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))

encoding_detected = result['encoding']
confidence = result['confidence']

print(f"👉 Encodage détecté : {encoding_detected} (Confiance : {confidence*100:.0f}%)")

# --- ÉTAPE 2 : La Lecture ---
try:
    # On essaie de lire avec l'encodage détecté
    df = pd.read_csv(filename, encoding=encoding_detected)
    
    print("\n✅ Fichier chargé avec succès !")
    print(f"Le tableau contient {df.shape[0]} lignes et {df.shape[1]} colonnes.")
    
    # Affichage des 5 premières lignes
    print("\nVoici un aperçu des données :")
    print(df.head())

except UnicodeDecodeError:
    print("❌ Erreur de décodage. L'encodage détecté n'était pas le bon.")
except FileNotFoundError:
    print(f"❌ Erreur : Je ne trouve pas le fichier '{filename}'. Vérifie qu'il est bien dans le même dossier que ce script python !")

# --- ÉTAPE 3 : (Optionnel) Sauvegarder en UTF-8 propre ---
# Si l'encodage d'origine n'était pas utf-8, on le convertit pour la prochaine fois
if encoding_detected != 'utf-8' and encoding_detected != 'ascii':
    output_filename = "ks-projects-clean.csv"
    df.to_csv(output_filename, encoding='utf-8', index=False)
    print(f"\n💾 Une copie propre a été sauvegardée sous '{output_filename}'")