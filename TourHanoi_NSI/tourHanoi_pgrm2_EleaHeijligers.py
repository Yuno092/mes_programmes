"""
Eléa Heijligers
Objectif: Implémenter le jeu de Hanoï
Programme itératif
"""
def hanoi(disque): #algoritme itératif
	
    l1=[5,4,3,2,1] #creation d'une liste avec 5 elements et deux autres vides
    l2=[]
    l3=[]

    total_num_of_moves=2**disque-1

    
    
    for i in range (1,total_deplacement+1):
        if total_deplacement%2==0:
            if i%3 == 1:
                if len(l1)>0 and len(l3)>0:
                    if l1[-1]<l3[-1]:
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 3)
                        
                        l3.append(l1.pop())
                    else:
                        print("Du piquet",3, "le rond", l3[-1] , "va au piquet", 1)
                        
                        l1.append(l3.pop())


                else:
                    if len(l1)>0:  
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 3)
                        
                        l3.append(l1.pop())
                    else:
                        print("Du piquet",3, "le rond", l3[-1] , "va au piquet", 1)
                        
                        l1.append(l3.pop())
        
            if i%3 == 2:
                if len(l2)>0 and len(l1)>0:
                    if l1[-1]<l2[-1]:
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 2)
                        
                        l2.append(l1.pop())
                    else:
                        print("Du piquet",2, "le rond", l2[-1] , "va au piquet", 1)
                        
                        l1.append(l2.pop())


                else:
                    if len(l1)>0:  
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 2)
                        
                        l2.append(l1.pop())
                    elif len(l2)>0:
                        print("Du piquet",2, "le rond", l2[-1] , "va au piquet", 1)
                        
                        l1.append(l2.pop())

            if i%3 == 0:
                if len(l2)>0 and len(l3)>0:
                    if l2[-1]<l3[-1]:
                        print("Du piquet",2, "le rond",l2[-1] , "va au piquet", 3)
                        
                        l3.append(l2.pop())
                    else:
                        print("Du piquet",3, "le rond", l3[-1] , "va au piquet", 2)
                        
                        l2.append(l3.pop())


                else:
                    if len(l2)>0:  
                        print("Du piquet",2, "le rond",l2[-1] , "va au piquet", 3)
                        
                        l3.append(l2.pop())
                    elif len(l3)>0:
                        print("Du piquet",3, "le rond", l3[-1] , "va au piquet", 2)
                        
                        l2.append(l3.pop())

        else:
            if i%3==1:
                if len(l1)>0 and len(l2)>0:
                    if l1[-1]<l2[-1]:
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 3)
                        
                        l2.append(l1.pop())
                    else:
                        print("Du piquet",3, "le rond", l2[-1] , "va au piquet", 1)
                        
                        l1.append(l2.pop())


                else:
                    if len(l1)>0:  
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 3)
                        
                        l2.append(l1.pop())
                    else:
                        print("Du piquet",3, "le rond", l2[-1] , "va au piquet", 1)
                        
                        l1.append(l2.pop())
        
            if i%3 == 2:
                if len(l3)>0 and len(l1)>0:
                    if l1[-1]<l3[-1]:
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 2)
                        
                        l3.append(l1.pop())
                    else:
                        print("Du piquet",2, "le rond", l3[-1] , "va au piquet", 1)
                        
                        l1.append(l3.pop())


                else:
                    if len(l1)>0:  
                        print("Du piquet",1, "le rond",l1[-1] , "va au piquet", 2)
                        
                        l3.append(l1.pop())
                    elif len(l3)>0:
                        print("Du piquet",2, "le rond", l3[-1] , "va au piquet", 1)
                        
                        l1.append(l3.pop())

            if i%3 == 0:
                if len(l3)>0 and len(l2)>0:
                    if l3[-1]<l2[-1]:
                        print("Du piquet",2, "le rond",l3[-1] , "va au piquet", 3)
                        
                        l2.append(l3.pop())
                    else:
                        print("Du piquet",3, "le rond", l2[-1] , "va au piquet", 2)
                        
                        l3.append(l2.pop())


                else:
                    if len(l3)>0:  
                        print("Du piquet",2, "le rond",l3[-1] , "va au piquet", 3)
                        
                        l2.append(l3.pop())
                    elif len(l2)>0:
                        print("Du piquet",3, "le rond", l2[-1] , "va au piquet", 2)
                        
                        l3.append(l2.pop())



hanoi(5)