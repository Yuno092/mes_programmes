"""
Eléa Heijligers
Objectif: Implémenter le jeu de Hanoï
Programme itératif pour un niveau 5
"""

cpt = 0  # on va compter le nombres de fois ou on va deplacer les disques 


def TourHanoi(cpt, n, depart, arrivee, transition):
    if (n == 1):
        print(cpt, ": deplacer le disque 1 de la tige", depart, "vers la tige", arrivee)
        cpt += 1
        return cpt
    cpt = TourHanoi(cpt, n-1, depart, transition, arrivee)
    print(cpt, ": deplacer le disque", n, "de la tige", depart, "vers la tige", arrivee)
    cpt += 1
    cpt = TourHanoi(cpt, n-1, transition, arrivee, depart)
    return cpt


TourHanoi(cpt, 5, 'centre', 'droite', 'gauche')