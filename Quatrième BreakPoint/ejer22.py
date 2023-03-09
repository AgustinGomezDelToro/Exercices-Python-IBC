# Ouverture du fichier data.txt en mode lecture
with open("data.txt", "r") as f:
    # Boucle pour lire chaque ligne du fichier
    for ligne in f:
        # Suppression du caractère de retour à la ligne en fin de ligne
        ligne = ligne.strip()
        # Vérification si la ligne est un email
        if "@" in ligne and ligne.endswith(".com"):
            print(f"{ligne} est un email valide.")
        else:
            print(f"{ligne} n'est pas un email valide.")
