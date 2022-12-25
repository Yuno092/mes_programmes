"""
Eléa Heijligers
Objectif: Implémenter le jeu de Hanoï
Programme récursif
"""

def TourHanoi(n, depart, arrivee, transition):
    if n == 1:  # si il n'y a qu'un seul disque alors on le déplace sur la tige d'arrivée
        print("Déplacer le disque 1 de la tige", depart, "vers la tige", arrivee)
        return
    TourHanoi(n-1, depart, transition, arrivee) 
    print("Déplacer le disque", n, "de la tige", depart, "vers la tige", arrivee)
    TourHanoi(n-1, transition, arrivee, depart)


n = 2 # nombre de disques
TourHanoi(n, 'centre', 'droite', 'gauche') # noms des tiges