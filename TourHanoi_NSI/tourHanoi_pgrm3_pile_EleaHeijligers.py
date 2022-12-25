"""
Eléa Heijligers
Objectif: Implémenter le jeu de Hanoï
Programme itératif utilisant des piles
"""
class Pile:  # création d'une classe Pile
    def __init__(self, nom):
        self.liste = []
        self.nom = nom

#### méthodes primitives############################
    # permet de rajouter un élément a la pile
    def empiler(self, valeur):
        self.liste.append(valeur)
        return self.liste

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
        if self.est_vide() == False :
            return self.liste.pop()

    # permet de lire le sommet de la pile
    def lire_Sommet(self):
        if self.est_vide() :
            return 10000
        return self.liste[-1]

    # permet de déterminer la hauteur de la pile
    def hauteur_Pile(self):
        return len(self.liste)

    def __str__(self):
        ch = ''
        print (self.nom)
        if self.est_vide(): 
            print ("->Liste vide")
            return ""
        for x in self.liste:
            ch = "\t" + str(x) + "\t" + "\n" + ch
        ch = ch + "_________________\n" 
        return ch

    # on vérifie l'égalité d'un pile sur sa liste et pas sur son nom
    # si les listes sont les mêmes, on considère les piles égales
    def equal (self, unePile):
        if self.liste == unePile.liste : 
            return True
        else :
            return False

####### Programme principal
####### définition des fonctions

# Permet d'affiche le contenu des tours
def printTour(Tour):
    print (Tour[0])
    print (Tour[1])
    print (Tour[2])
    print ("################\n")

# Permet de connaitre la Pile dans la tour qui contient le plus petit element
def tourPPElement (Tour):
    # si une tour/tige est vide alors on considère qu'elle n'a pas le plus petit element
    # on lui met une grande valeur pour être sure que le disque sera plus petit
    if Tour[0].est_vide() == False:
        valTour0 = int(Tour[0].lire_Sommet())
    else :
        valTour0 = 10000
    
    if Tour[1].est_vide() == False :
        valTour1 = int(Tour[1].lire_Sommet())
    else :
        valTour1 = 10001

    if Tour[2].est_vide() == False :
        valTour2 = int(Tour[2].lire_Sommet())
    else :
        valTour2 = 10002

    if valTour0 < valTour1 and valTour0 < valTour2 : 
        return 0
    if valTour1 < valTour0 and valTour1 < valTour2 : 
        return 1
    else: 
        return 2

# Permet de bouger un disque d'une tige/pile à l'autre
def bougeDisque (pile1, disque1, pile2, disque2, pile3) :
    if (disque1< disque2):
        pile2.empiler(pile1.depiler())
        print ("On déplace le disque", disque1, "de la tige ", pile1.nom ,"vers la tige", pile2.nom)
    elif (disque1 > disque2):
        pile1.empiler(pile2.depiler())
        print ("On déplace le disque", disque2, "de la tige ", pile2.nom ,"vers la tige", pile1.nom)
    else:
        print ("ICI :", pile1, disque1, "\n", pile2, disque2,"\n", pile3, "FIN")

        pile1.empiler(pile3.depiler())
        print ("On déplace le disque", pile3.lire_Sommet(), "de la tige ", pile3.nom ,"vers la tige", pile1.nom)

# Initialisation d'une tour
def initTour(nom, nbDisques) :
    tige = Pile(nom)
    for i in range (nbDisques, 0, -1):
        tige.empiler(str(i))
    return tige 

##############################################
##############################################
##############################################
##############################################

# Initialisation
n = 5 # nombre de disques

# la tour de départ contient n éléments
depart = initTour("Depart", n)

# les tours d'arrivée et de transition sont vides
arrivee = Pile("Arrivee")
transition = Pile("Transition")

# On copie dans une autre pile la pile de départ
# pour pouvoir la comparer avec la tour d'arrivée
resultatAttendu = initTour("resultatAttendu", n)


# Tour contient 3 piles, la premiere avec les disques et les autres sont vides
Tour = [depart, transition, arrivee]
printTour(Tour)
#print ("le plus petit disque est dans la tour :",tourPPElement(Tour))
#print ("le plus grand disque est dans la tour :",tourPGElement(Tour))

tigeDACote = 0
i=0
pair = True # on positionne pair arbitrairement
while resultatAttendu.equal(arrivee) == False :
    i = i+1
    #printTour(Tour)

    tigeInit = tigeDACote
    # si nb disques est pair
    if n % 2 == 0 :
        tigeDACote = tigeDACote+1
        if tigeDACote == 3 : 
            tigeDACote = 0
            pair = True
    else : 
        tigeDACote = tigeDACote-1
        if tigeDACote == -1 : 
            tigeDACote = 2
            pair = False # dans ce cas, c'est impair et on va dans le sens inverse
    
    # on déplace le disque le plus petit sur la tour suivante
    # si on arrive à la dernière pile, on repasse à la première
    Tour[tigeDACote].empiler(Tour[tourPPElement(Tour)].depiler())
    print ("On déplace le disque 1 de la tige",Tour[tigeInit].nom,"vers la tige", Tour[tigeDACote].nom)
    #printTour(Tour)

    disqueInit = Tour[tigeInit].lire_Sommet()

    if resultatAttendu.equal(arrivee) == False :
        if pair == True:
            # on recupere le disque de la tige après la tige ou on vient de déposer le disque
            if tigeDACote == 2 :
                disqueSuivant = Tour[0].lire_Sommet()
                bougeDisque (Tour[0], int(disqueSuivant), Tour[tigeInit], int(disqueInit), Tour[tigeDACote])
            else : 
                disqueSuivant = Tour[tigeDACote+1].lire_Sommet()
                bougeDisque (Tour[tigeDACote+1], int(disqueSuivant), Tour[tigeInit], int(disqueInit), Tour[tigeDACote])
            # le pb est là
            #if int(disqueSuivant) == int(disqueInit) : print ("pas bon !!!!!")
        else : # impair
            # on recupere le disque de la tige après la tige ou on vient de déposer le disque
            if tigeDACote == 0 :
                disqueSuivant = Tour[2].lire_Sommet()
                bougeDisque (Tour[2], int(disqueSuivant), Tour[tigeInit], int(disqueInit), Tour[tigeDACote])
            else : 
                disqueSuivant = Tour[tigeDACote-1].lire_Sommet()
                bougeDisque (Tour[tigeDACote-1], int(disqueSuivant), Tour[tigeInit], int(disqueInit), Tour[tigeDACote])
            # le pb est là
            #if int(disqueSuivant) == int(disqueInit) : print ("pas bon !!!!!")

printTour(Tour)