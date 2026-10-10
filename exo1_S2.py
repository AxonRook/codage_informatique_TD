# Comparaison d'une valeur "X"
x = int(input("Entrez une valeur entière (X) : "))

# X inférieur ou égal à 10
if x <= 10:
    print("La valeur est inférieure ou égale à 10, et donc très faible.")

# X supérieur à 10 et inférieur ou égal à 30
elif x <= 30:
    print("La valeur est supérieure à 10 et inférieure ou égale à 30, et donc faible.")
    # ici on sait déjà que x > 10

# X supérieur à 30 et inférieur ou égal à 60
elif x <= 60:
    print("La valeur est supérieure à 30 et inférieure ou égale à 60, et donc moyenne.")
    # X > 30

# X supérieur à 60 et inférieur ou égal à 90
elif x <= 90:
    print("La valeur est supérieure à 60 et inférieure ou égale à 90, et donc bonne.")
    # X > 60

# X supérieur à 90
else:
    print("La valeur est supérieure à 90, et donc très bonne.")
    # X > 90