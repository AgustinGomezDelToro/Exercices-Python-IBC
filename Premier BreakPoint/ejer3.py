import math

# Saisie du flottant
nombre = float(input("Entrez un nombre : "))

# Vérification du signe
if nombre >= 0:
    # Calcul et affichage de la racine carrée
    racine = math.sqrt(nombre)
    print(f"La racine carrée de {nombre} est {racine:.2f}.")
else:
    # Affichage du message d'erreur
    print("Erreur : le nombre saisi est négatif.")

