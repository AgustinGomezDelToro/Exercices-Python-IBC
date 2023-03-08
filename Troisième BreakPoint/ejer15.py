# Définition de la liste
liste = [17, 38, 10, 25, 72]

# Tri de la liste
liste.sort()
print(liste)

# Ajout de l'élément 12 à la liste
liste.append(12)
print(liste)

# Inversion de la liste
liste.reverse()
print(liste)

# Recherche de l'indice de l'élément 17
print(liste.index(17))

# Suppression de l'élément 38 de la liste
liste.remove(38)
print(liste)

# Affichage de la sous-liste du 2e au 3e élément
print(liste[1:3])

# Affichage de la sous-liste du début au 2e élément
print(liste[:2])

# Affichage de la sous-liste du 3e élément à la fin de la liste
print(liste[2:])

# Affichage de la sous-liste complète de la liste
print(liste[:])
