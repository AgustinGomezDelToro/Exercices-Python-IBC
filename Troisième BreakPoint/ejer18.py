chaine = input("Entrez une chaîne : ")

# Vérification si c'est un email
if "@" in chaine and "." in chaine and chaine.index("@") < chaine.index(".") and len(chaine.split(".")[-1]) <= 3:
    print("La chaîne est un email valide.")
else:
    print("La chaîne n'est pas un email valide.")