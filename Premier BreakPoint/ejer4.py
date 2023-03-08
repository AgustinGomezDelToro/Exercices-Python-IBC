# Saisie des deux mots
mot1 = input("Entrez le premier mot : ")
mot2 = input("Entrez le deuxième mot : ")

# Comparaison des mots
if mot1 < mot2:
    print(f"Le mot {mot1} est avant le mot {mot2} dans l'ordre lexicographique.")
elif mot1 > mot2:
    print(f"Le mot {mot2} est avant le mot {mot1} dans l'ordre lexicographique.")
else:
    print("Les deux mots sont identiques.")
