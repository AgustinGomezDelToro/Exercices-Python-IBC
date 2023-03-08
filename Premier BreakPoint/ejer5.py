
pSeuil = 2.3
vSeuil = 7.41

#pression et volume
pression = float(input("Entrez la pression courante de l'enceinte : "))
volume = float(input("Entrez le volume courant de l'enceinte : "))

# Vérif
if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat : la pression et le volume sont supérieurs aux seuils.")
elif pression > pSeuil:
    print("Demande d'augmenter le volume de l'enceinte : la pression est trop élevée.")
elif volume > vSeuil:
    print("Demande de diminuer le volume de l'enceinte : le volume est trop élevé.")
else:
    print("Tout va bien : la pression et le volume sont en dessous des seuils.")
