def annee():
    nbEcureuilGris=200
    nbEcureuilRoux=20000
    annee=0

    augmentationEcureuilGrisAnnuel=12/100
    diminutionEcureuilRouxAnnuel=5/100

    while (nbEcureuilGris<nbEcureuilRoux):
        nbEcureuilGris= round (nbEcureuilGris+nbEcureuilGris*augmentationEcureuilGrisAnnuel)
        nbEcureuilRoux= round(nbEcureuilRoux-nbEcureuilRoux*diminutionEcureuilRouxAnnuel)
        annee=annee+1
        print ("Au bout de "+str(annee)+" années, il y aura "+str( nbEcureuilRoux)+" écureuils roux et "+ str(nbEcureuilGris) + " écureuils gris")
    return ("Au bout de "+str(annee)+" années, il y aura "+str( nbEcureuilRoux)+" écureuils roux et "+ str(nbEcureuilGris) + " écureuils gris")

exec(annee())