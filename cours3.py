mot_de_passe = input("Quel est ton mot de passe ? ")
longueur_du_mot_de_passe = len(mot_de_passe)#Determiner la longueur de la chaine de caractères

print (f"Ton mot de passe fait {longueur_du_mot_de_passe} caractères.")
if longueur_du_mot_de_passe<=8:
  print("Ce mot de passe est faible :(")

elif longueur_du_mot_de_passe<12:
  print("Ce mot de passe est moyen :|")

else:
  print("Ce mot de passe est fort :)")


