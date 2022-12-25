"""
Eléa Heijligers
05/12/2022
Objectif : Implémenter une pile en Python, en utilisant le type List
particularité :
intégrer obligatoirement le code suivant à la fin de la classe :
def __str__(self):
    ch = ''
    for x in self.valeurs:
        ch = "|\t" + str(x) + "\t|" + "\n" + ch
        ch = "\nEtat de la pile:\n" + ch
    return ch
Une classe Piles contiendra les opérations élémentaires des piles, ainsi
qu’une fonction permettant de lire le sommet de la pile et une autre de
déterminer la hauteur de la pile.
"""


class Piles:  # création d'une classe Piles
    def __init__(self):
        self.liste = []

#### méthodes primitives############################
    # permet de rajouter un élément a la pile
    def empiler(self, valeur):
        self.liste.append(valeur)

    # permet de vérifier si la pile est vide
    # renvoie True si elle l'est et False dans le cas contraire
    def est_vide(self):
        longueur = len(self.liste)
        if longueur != 0:
            return False
        else:
            return True

    # permet de retirer un élément de la pile
    def depiler(self):
        if self.liste:
            return self.liste.pop()

    # perme de creer une pile vide
    def creer_pile(self):
        self.liste = []
        return self.liste

############### méthodes secondaires###########
    # permet de lire le sommet de la pile
    def lire_Sommet(self):
        return self.liste[-1]

    # permet de déterminer la hauteur de la pile
    def hauteur_Pile(self):
        return len(self.liste)

    # censée renvoyer une représentation sous forme de chaîne de caractères d'un objet
    def __str__(self):
        ch = ''
        for x in self.liste:
            ch = "|\t" + str(x) + "\t|" + "\n" + ch
            ch = "\nEtat de la pile:\n" + ch
        return ch


"""
p = Piles()
assert (p.est_vide())
p.empiler(1)
assert (not p.est_vide())
assert (p.hauteur_Pile() == 1)
p.empiler("2")
p.empiler(3)
print("la pile contient", p)
p.depiler()
p.empiler(82)
print("la pile est vide ?", p.est_vide())
print("Et enfin, la pile contient", p)
print("l'élement au sommet de la pile est", p.lire_Sommet())
print("la pile contient", p.hauteur_Pile(), "éléments")
"""
