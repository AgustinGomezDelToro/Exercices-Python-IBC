# Boucle de saisie filtrée
nombre = 0

while nombre < 1 or nombre > 10:
    nombre = int(input("Entrez un entier entre 1 et 10 : "))

# Affichage de la saisie
print("Vous avez saisi le nombre", nombre)
