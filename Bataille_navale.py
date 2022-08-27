from operator import truediv
import random

#Impression de la grille
def imprimeGrille(uneGrille):
    for row in uneGrille:
        print(' '.join([str(elem) for elem in row]))

# cette fonction vérifie si le coup joué est gagnant
def verifCoup(x, y, grille):
    if grille[x][y] == 1 : return "touché"
    else: return "loupé"

# cette fonction vérifie que la taille de la grille saisie est un entier compris entre 5 et 10
def verifTailleGrille(taille):
    # TODO taille doit êtr eun entier
    taille = int(taille)
    # taille doit être entre 5 et 10
    if taille > 4 and taille < 11:
        return True
    else: 
        return False

gainJoueur = 20
finPartie = False

print("***Bienvenue à la bataille navale***\n")
print(f"Vous avez {gainJoueur}€\n")
jouer= input("Commencer une partie ? (O/N) ")

while jouer == "O" or jouer == "o":

    tailleGrille= 0
    while verifTailleGrille(tailleGrille) == False:
        tailleGrille = input ("Indiquez la taille de la grille (entre 5 et 10):")

    tailleGrille=int(tailleGrille)

    # j'initialise la grille avec des 0 ainsi que la grille des coups joués par l'ordi
    grille= [0]*tailleGrille
    grilleCoupsPNJ = [0]*tailleGrille

    for i in range (tailleGrille):
        grille [i] = [0]*tailleGrille
        grilleCoupsPNJ [i] = [0]*tailleGrille


    # je place aléatoirement le bateau du PNJ
    randX = random.randint(0,tailleGrille-1)
    randY = random.randint(0,tailleGrille-1)
    grille[randX][randY]=1



    imprimeGrille(grille)

    #l'utilisateur indique où il a placé son bateau. L'information n'est pas mémorisée 
    input("Indique où est placé ton bateau ? (ligne,colonne) ")

    #le joueur indique combien il mise sur cette partie
    mise = int(input(f"Combien mises-tu sur cette partie ? (doit être inférieur ou égal à {gainJoueur}) "))

    partieFinie = False
    gagnant = "" # le gagnant peut être le joueur ou le PNJ, vide tant que personne n'a gagné

    #c'est toujours le joueur qui commence
    print("C'est parti !\n")

    while partieFinie==False:
        #c'est au joueur de jouer; on enlève 1 car notre grille commence à 0
        print("A toi de jouer !\n")
        ligne=int(input("Indique la ligne:"))-1
        colonne=int(input("Indique la colonne:"))-1
        
        # le joueur a t il touché ou proche ou loupé ?
        if verifCoup (ligne, colonne, grille) == "touché" : 
            partieFinie = True
            gagnant = "joueur"
        else: 
            print ("loupé\n")    
            #c'est au PNJ de jouer
            # on vérifie que le coup n'a pas déjà été joué
            randLigne = random.randint(1,tailleGrille)
            randColonne = random.randint(1,tailleGrille)
            while grilleCoupsPNJ[randLigne][randColonne] == 1 :
                randLigne = random.randint(1,tailleGrille)
                randColonne = random.randint(1,tailleGrille)

            # on mémorise le nouveau coup joué
            grilleCoupsPNJ[randLigne][randColonne] = 1
            jeuPNJ = input(f"Ton bateau est sur la ligne {randLigne} et sur la colonne {randColonne} (O/N)?\n")
            if jeuPNJ == "O" or jeuPNJ == "o" : 
                partieFinie = True
                gagnant = "PNJ"


    print (f"La partie est finie. Le gagnant est le {gagnant}")
    if gagnant=="joueur":
        gainJoueur += mise
        if gainJoueur == 2000:
            print("Bravo : Tu viens de gagner une pizza !\n")
    else :
        gainJoueur -= mise
        if gainJoueur == 0 :
            print("Tu n'as plus d'argent !")
            finPartie = True
    
    print(f"Il te reste {gainJoueur}€")

    if finPartie == True :
        print ("C'est perdu !!")
        jouer= "N"
    else :
        jouer=input("Refaire une partie ? (O/N) ")

print("Merci d'avoir joué avec moi")

