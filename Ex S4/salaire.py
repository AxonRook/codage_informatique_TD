# Fonction du salaire annuel net
def salaire_net_annuel(brut, taux):
    return brut * (1 - taux / 100)

# Fonction du salaire mensuel net
def salaire_net_mensuel(net_annuel):
    return net_annuel / 12