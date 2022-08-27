from math import *
a=1 # borne d'encadrement basse
b=1 # borne d'encadrement haute
k=0 # nombre de répétitions de l'amplitude
n=2 # modifier la valeur pour définir l'amplitude, plus n est grand, plus le calcul est long
amplitude=10**(-n)

print("avec n="+str(n))
print("l'amplitude="+str(amplitude))
while b**2<2:
  a=b
  b=1+k*amplitude
  k=k+1
  #print("k="+str(k))  
print("racine(2) et compris entre a= "+str(round(a,n))+" et b="+str(b))
print("pour rappel racine(2)="+str(sqrt(2)))
