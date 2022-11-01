"""Elea Heijligers
19/09/2022
Le but est de creer un module
fonctions:
-taux de variation
-indice des prix
-productivité globale des facteurs(PGF)
-chiffre d'affaire
-valeur ajoutée
-production en volume
fonction constante: règle des 70
version 1
"""
#fonction qui calcule le taux de variation en prenant deux valeurs, valeur d'arrivée et valeur de départ en paramètre
def tauxvar(ValeurA,ValeurD):
    return ((ValeurA-ValeurD)/ValeurD)*100

def pgf(production,facteurL,facteurK):
    return (production/facteurL+facteurK)

def indicePrix(ValeurA,ValeurD):
    return ((ValeurA-ValeurD)/ValeurD)*100

def chiffreAffaire(quantiteProduitVendu,prixVente):
    return quantiteProduitVendu*prixVente

def valeurAjoutee(chiffreAffaire,consoIntermediaire):
    return chiffreAffaire-consoIntermediaire

def productionEnVolume(ProductionEnValeur,IndiceDesPrix):
        return (ProductionEnValeur/IndiceDesPrix)*100

def regle70(tauxCroissanceAnnuelMoy):
    return tauxCroissanceAnnuelMoy/70
