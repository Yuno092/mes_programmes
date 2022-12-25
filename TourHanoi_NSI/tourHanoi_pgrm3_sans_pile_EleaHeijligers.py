#############################################################################
def deplace(nomA, A, nomB, B):
    """déplace un disque d'une des 2 tours vers l'autre tour
       sur un disque plus grand ou sur une tour vide
    """
    if len(A)>0 and (len(B)==0 or A[-1]<B[-1]):
        print("Déplace {} => {}".format(nomA, nomB))
        B.append(A.pop())
    else:
        print("Déplace {} => {}".format(nomB, nomA))
        A.append(B.pop())
 
#############################################################################
def _hanoi(nbdisques, tour1, tour2, tour3):
    global nbcoups
 
    if nbdisques%2==0:
        # solution nbdisques pair
        while len(tour1)+len(tour2)!=0:
            #----------------------------------------------------------------
            # somme=3: déplacement 1=>2 ou 2=>1
            nbcoups += 1
            deplace("tour1", tour1, "tour2", tour2)
            print(nbcoups, tour1, tour2, tour3, '\n')
            #----------------------------------------------------------------
            # somme=4: déplacement 1=>3 ou 3=>1
            nbcoups += 1
            deplace("tour1", tour1, "tour3", tour3)
            print(nbcoups, tour1, tour2, tour3, '\n')
            #----------------------------------------------------------------
            # somme=5: déplacement 2=>3 ou 3=>2
            nbcoups += 1
            deplace("tour2", tour2, "tour3", tour3)
            print(nbcoups, tour1, tour2, tour3, '\n')
    else:
        # solution nbdisques impair
        while len(tour1)+len(tour2)!=1:
            #----------------------------------------------------------------
            # somme=4: déplacement 1=>3 ou 3=>1
            nbcoups += 1
            deplace("tour1", tour1, "tour3", tour3)
            print(nbcoups, tour1, tour2, tour3, '\n')
            #----------------------------------------------------------------
            # somme=3: déplacement 1=>2 ou 2=>1
            nbcoups += 1
            deplace("tour1", tour1, "tour2", tour2)
            print(nbcoups, tour1, tour2, tour3, '\n')
            #----------------------------------------------------------------
            # somme=5: déplacement 2=>3 ou 3=>2
            nbcoups += 1
            deplace("tour2", tour2, "tour3", tour3)
            print(nbcoups, tour1, tour2, tour3, '\n')
        #--------------------------------------------------------------------
        # dernier déplacement pour somme impaire
        nbcoups += 1
        print("Déplace tour1 => tour3")
        tour3.append(tour1.pop())
        print(nbcoups, tour1, tour2, tour3, '\n')
 
#============================================================================
def hanoi(nbdisques):
 
    # crée les tours avec les disques demandés sur la tour d'origine
    tour1 = [i for i in range(nbdisques, 0, -1)]
    tour3 = []
    tour2 = []
 
    # affiche la situation de départ pour les 3 tours
    print("Etat des 3 tours au départ, avec", nbdisques, "disques sur la tour origine:")
    print("origine:", tour1, "intermédiaire:", tour2, "destination:", tour3)
    print()
 
    _hanoi(nbdisques, tour1, tour3, tour2)
 
############################################################################# 

nbcoups = 0 # variable globale
n = 3 # nombre de disques à déplacer
hanoi(n)
