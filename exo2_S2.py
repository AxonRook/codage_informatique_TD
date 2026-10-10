# Saisie des variables
prenom = input("Entrez votre prénom : ")
note = float(input("Entrez votre note : "))

# Calcul de la mention en fonction de la note
mention = ""
if note <= 12:
    mention = "pas de mention"
elif note <= 14:
    mention = "Assez bien"
elif note <= 16:
    mention = "Bien"
else:
    mention = "Très bien"

# Affichage du message
if prenom == "Julie":
    print(f"Bienvenue, {mention}".strip())
elif prenom == "Paul":
    print(f"Bonjour, {mention}".strip())
else:
    print("A bientôt")