# Demande du nombre de chaînes de caractères à enregistrer
x = int(input("Entrez le nombre de chaînes de caractères à enregistrer : "))

# Ouverture du fichier data.txt en mode écriture
with open("data.txt", "w") as f:
    # Boucle pour demander x chaînes de caractères et les enregistrer dans le fichier
    for i in range(x):
        chaine = input(f"Entrez la chaîne de caractères n°{i+1} : ")
        f.write(chaine + "\n")

# Confirmation de l'enregistrement
print(f"{x} chaînes de caractères ont été enregistrées dans le fichier data.txt.")
