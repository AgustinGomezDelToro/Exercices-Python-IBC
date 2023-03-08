# Saisie de la chaîne
chaine = input("Entrez une chaîne : ")

# Inversion de la chaîne
inverse = chaine[::-1]

# Vérification si c'est un palindrome
if chaine == inverse:
    print("La chaîne est un palindrome.")
else:
    print("La chaîne n'est pas un palindrome.")
