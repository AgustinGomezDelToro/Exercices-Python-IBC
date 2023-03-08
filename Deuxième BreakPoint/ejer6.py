# Saisie de la chaîne de caractères
chaine = input("Entrez une chaîne de caractères : ")

# Vérification de l'email
if "@" in chaine and chaine.endswith(".com"):
    print("Ceci est un email valide.")
else:
    print("Ceci n'est pas un email valide.")
