def cube(x):
    return x ** 3

def volumeSphere(r):
    return (4/3) * 3.14159 * cube(r)

# Test de la fonction volumeSphere avec un rayon de 2
rayon = 2
volume = volumeSphere(rayon)
print(f"Le volume de la sphère de rayon {rayon} est {volume}.")
