def compterMots(chaine):
    # Création d'un dictionnaire vide pour stocker les fréquences
    freq = {}

    # Séparation de la chaîne en mots à l'aide de la méthode split()
    mots = chaine.split()

    # Boucle pour compter la fréquence de chaque mot
    for mot in mots:
        if mot in freq:
            freq[mot] += 1
        else:
            freq[mot] = 1

    # Renvoi du dictionnaire de fréquences
    return freq
# Appel de la fonction compterMots() sur une chaîne de caractères
chaine = "Le chat mange la souris, le chat dort, le chat miaule."
freq = compterMots(chaine)

# Affichage du dictionnaire de fréquences
print(freq)

