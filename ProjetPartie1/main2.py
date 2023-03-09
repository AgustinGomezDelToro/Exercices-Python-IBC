class AB:
    def __init__(self, racine=None, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    # Override de la méthode str pour afficher les attributs de l'objet
    def __str__(self):
        return f"Racine : {self.racine}\nGauche : {self.gauche}\nDroite : {self.droite}"

    def setGauche(self, gauche):
        self.gauche = gauche

    def setDroite(self, droite):
        self.droite = droite

    def setRacine(self, racine):
        self.racine = racine

    def getGauche(self):
        return self.gauche

    def getDroite(self):
        return self.droite

    def getRacine(self):
        return self.racine

    def estVide(self):
        if self.racine == None and self.gauche == None and self.droite == None:
            return True
        else:
            return False

    # La taille d'un arbre est le nombre de noeuds de l'arbre
    def taille(self):
        taille = 0
        if self.getGauche() != None:
            taille += self.getGauche().taille()
        if self.getDroite() != None:
            taille += self.getDroite().taille()
        return taille + 1

    # Parcours prefixe : on visite la racine, puis le sous-arbre gauche, puis le sous-arbre droit
    def prefixe(self):
        parcours_prefixe = ""
        parcours_prefixe += str(self.getRacine()) + " "
        if self.getGauche() != None:
            parcours_prefixe += self.getGauche().prefixe()
        if self.getDroite() != None:
            parcours_prefixe += self.getDroite().prefixe()
        return parcours_prefixe

    # Parcours postfixe : on visite la racine, puis le sous-arbre gauche, puis le sous-arbre droit
    def postfixe(self):
        parcours_postfixe = ""
        if self.getGauche() != None:
            parcours_postfixe += self.getGauche().postfixe()
        if self.getDroite() != None:
            parcours_postfixe += self.getDroite().postfixe()
        parcours_postfixe += str(self.getRacine()) + " "
        return parcours_postfixe

    def infixe(self):
        parcours_infixe = ""
        if self.getGauche() is not None:
            parcours_infixe += self.getGauche().infixe()
        parcours_infixe += str(self.getRacine()) + " "
        if self.getDroite() is not None:
            parcours_infixe += self.getDroite().infixe()
        return parcours_infixe

    def estABR(self):
        if self.estVide():
            return True
        if self.gauche != None and self.racine < self.gauche.racine:
            return False
        if self.droite != None and self.racine > self.droite.racine:
            return False
        return True

    def hauteur(self):
        if self.estVide():
            return 0
        else:
            hauteur_gauche = 0
            hauteur_droite = 0
            if self.getGauche() != None:
                hauteur_gauche = self.getGauche().hauteur()
            if self.getDroite() != None:
                hauteur_droite = self.getDroite().hauteur()
            return max(hauteur_gauche, hauteur_droite) + 1

    def estEquilibre(self):
        if self.estVide():
            return True
        hauteur_gauche = 0
        hauteur_droite = 0
        if self.getGauche() is not None:
            hauteur_gauche = self.getGauche().hauteur()
        if self.getDroite() is not None:
            hauteur_droite = self.getDroite().hauteur()
        if abs(hauteur_gauche - hauteur_droite) > 1:
            return False
        return True


# exercice 3
A1 = AB()
print(A1.estVide())  # Doit retourner True

# exercice 4
A2 = AB(5)
print(A2.estVide())  # Doit retourner False

# exercice 5
A3 = AB(3)

# exercice 6
A2.setGauche(A3)

# exercice 7
A1 = AB(5, AB(3), AB(8))

A2 = AB(12)

A3 = AB(5)

# Atest = AB(10, AB(A1), AB(A2))
Atest = AB(10, AB(5, AB(3), AB(8)), AB(12))

print(Atest.estVide())  # Doit retourner False

# exercice 8
# Utilisation de l'arbre Atest créé précédemment
print(Atest.taille())  # Doit retourner 5

# exercice 9
print(Atest.taille())  # Doit retourner 5

# exercice 10
# La méthode taille() est déjà codée en récursif dans la classe AB.


# exercice 11
# Utilisation de l'arbre Atest créé précédemment
print(Atest.prefixe())  # Doit afficher : "10 5 3 8 12"

# exercice 13
# Test des deux autres parcours
print(Atest.postfixe())  # Doit afficher : "3 8 5 12 10"
print(Atest.infixe())  # affichera : 3 5 8 10 12

# exercice 14
print(Atest.hauteur())  # Imprime 2

# exercice 15
print(Atest.estABR())  # Imprime True o False

# exercice 16
print(Atest.estEquilibre())  # Imprime True o False
