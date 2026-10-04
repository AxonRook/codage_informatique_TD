# Dictionnaire des fruits
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Ajout de la clé kiwi à la liste (avec la valeur "vert")
fruits["kiwi"] = "vert"

# Stockage de la valeur de la clé banane dans une variable
couleur_banane = fruits["banane"]

# Modificaion de la couleur de la pomme
fruits["pomme"] = "vert"

# Retrait de la clé banane du dictionnaire
del fruits["banane"]

# Affichage des clés restantes dans le dictionnaire
print("Clés restantes dans le dictionnaire :", list(fruits.keys()))