# Importation du fichier module salaire
import salaire

# Définition de la fonction main
def main():
    # Saisie du salaire annuel brut et du taux de prélèvement obligatoire
    brut = float(input("Salaire annuel brut (€) : "))
    taux = float(input("Taux de prélèvement obligatoire (%) : "))

    # Calcul du salaire annuel net et du salaire mensuel net
    net_annuel = salaire.salaire_net_annuel(brut, taux)
    net_mensuel = salaire.salaire_net_mensuel(net_annuel)

    # Affichage du salaire annuel net et du salaire mensuel net
    print(f"Salaire mensuel net : {net_mensuel:.2f} €")

# Fonction main
if __name__ == "__main__":
    main()