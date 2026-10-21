#Récupération du prénom et nom avant @
def extraire_identite(mail):
    pos=mail.find("@")
    return mail[:pos]

#Remplacement du point par un espace et conversion en majuscules
def format_identite(patronyme):
    text=patronyme.replace("."," ")
    return text.upper()

#Saisie des infos et affichage du résultat
def main():
    adress_mail=input("Veuillez saisir votre adresse mail : ")
    identite=extraire_identite(adress_mail)
    nom=format_identite(identite)
    print("Votre patronyme est :", nom)

if __name__ == "__main__":
    main()