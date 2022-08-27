from random import randint
nbLancers=0
des=0
maxLancers=0 
while nbLancers<1000:
  nbLancers=0
  des=0
  
  while des<50:
    des=randint (1,50)
    #print("le dé est sur:"+str(des))
    nbLancers = nbLancers+1
    if nbLancers > maxLancers: 
      maxLancers=nbLancers
      print ("maxlancers =" + str(maxLancers))
print("nombre de lancers= "+str(nbLancers))
