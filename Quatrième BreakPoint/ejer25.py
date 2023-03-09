def somme(a, b, c):
    return a + b + c


# Définition d'un tuple de trois nombres
t = (3, 7, 9)

# Appel de la fonction somme en décompressant le tuple
resultat = somme(*t)

# Affichage du résultat
print(f"La somme des nombres {t} est {resultat}.")
