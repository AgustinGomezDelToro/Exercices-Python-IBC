# Saisie du nom et de l'âge en tant que chaînes de caractères
nom_str = input("Entrez votre nom : ")
age_str = input("Entrez votre âge : ")

# Transtypage en str pour nom et en int pour âge
nom = str(nom_str)
age = int(age_str)

# Affichage des données saisies
print("Vous vous appelez", nom, "et vous avez", age, "ans.")
