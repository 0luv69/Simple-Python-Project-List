

# end="", this avoids from going new line

def alphabate(alpha1):

    # it prints A
    if alpha1 =="A":      
            for i in range(6):
                    for j in range (5):
                        if i == 0:
                            if j == 2:
                                print("A",end="  ")
                            else:
                                print(" ",end="  ")
                        elif i ==1:
                            if j == 1 or j == 3:
                                print("A",end="  ")
                            else:
                                print(" ",end="  ")  
                        elif i == 2:
                            if j == 0 or j == 4:
                                print("A", end="  ")
                            else:
                                print(" ", end="  ")
                        elif i == 3:
                            print("A",end="  ")          
                        elif i == 4 or i == 5:
                            if j == 0 or j == 4:
                                print("A", end="  ")
                            else:
                                print(" ", end="  ")     
                    print("")  
            print("\n")

    #it prints B
    elif alpha1 =="B":  
            for i in range(8):
                if i == 1 or i == 2 or i== 5 or i == 6:
                    for j in range(5):
                        if j == 1 or j == 2 or j == 3:
                            print(" ",end="  ") 
                        else:
                            print("B",end="  ")    
                else:
                    for j in range(4):
                        print('B', end="  ")
                        
                print("")
            print("\n")

    #it prints c
    elif alpha1 =="C":
            for i in range (5):
                for j in range(5):
                    if i == 4 or i == 0:
                        print("C", end="  ")
                    else:
                        if j == 0:
                            print("C",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
            print("\n") 

    # it prints D
    elif alpha1 =="D":  
            for i in range(7):
                for j in range(5):
                    if i == 0 or i == 6:
                        if j <=2:
                            print("D", end="  ")
                    elif i == 1 or i == 5:
                        if j == 0 or j == 3:
                            print("D", end="  ")
                        else:
                            print(" ",end="  ")     
                    elif i == 2 or i==4:
                        if j == 0 or j == 4:
                            print("D", end="  ")
                        else:
                            print(" ",end="  ") 
                    elif i == 3 :
                        if j == 0 or j == 4:
                            print("D", end="  ")
                        else:
                            print(" ",end="  ")        
                        
                    
                print(' ')
            print("\n")

    # it prints E
    elif alpha1 =="E":
            for i in range (7):
                for j in range(5):
                    if i == 6 or i == 0 or i == 3:
                        print("E", end="  ")
                    else:
                        if j == 0:
                            print("E",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
            print("\n")  

    # it prints F
    elif alpha1 =="F":
            for i in range (7):
                for j in range(5):
                    if i == 0 or i == 3:
                        print("F", end="  ")
                    else:
                        if j == 0:
                            print("F",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
            print("\n")

    # it prints G
    elif alpha1 =="G":
        for i in range (7):
                for j in range(5):
                    if i == 6 or i == 0:
                        print("G", end="  ")
                    elif i == 1 or i == 2:
                        if j == 0:
                            print("G",end="  ")    
                        else:
                            print(" ",end="  ") 
                    elif  i == 5:
                        if j == 0 or j == 4:
                            print("G",end="  ")    
                        else:
                            print(" ",end="  ")     
                    elif i == 4:
                        if j == 0 or j == 4 or j == 2:
                            print("G",end="  ")    
                        else:
                            print(" ",end="  ")
                    elif i ==3: 
                        if j == 1:
                            print(" ",end="  ")    
                        else:
                            print("G",end="  ")                
                print(" ")
        print("\n") 

    # it prints H     
    elif alpha1 =="H":
        for i in range (7):
                for j in range(5):
                    if i ==3 :
                        print("H", end="  ")
                    else:
                        if j == 0 or j == 4:
                            print("H",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
        print("\n") 

    # it prints I     
    elif alpha1 =="I":
        for i in range (5):
                for j in range(5):
                    if i == 4 or i == 0:
                        print("I", end="  ")
                    else:
                        if j == 2:
                            print("I",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
        print("\n") 
    
    # it prints J
    elif alpha1 =="J":
            for i in range(7):
                for j in range (5):
                    if i == 0:
                        print("J", end="  ")
                    elif i ==1 or i == 2 or i == 3 or i== 4:
                        if j == 0 or j ==1:
                            print(" ", end= "  ")
                        elif j == 4:
                            print("J", end = "  ")
                    elif i == 5:
                        if j == 0 or j == 2:
                            print("J", end="  ")
                        else:
                            print(" ", end= "  ")
                    elif i == 6:
                        if j == 1 or j == 2:
                            print("J", end="  ")  
                        else:
                            print(" ", end= "  ")                  
                print("")
            print("\n")

    # it prints K     
    elif alpha1 =="K":
        for i in range (7):
                for j in range(5):
                    if i == 0 or i == 6:
                        if j == 0 or j ==4:
                            print("K", end="  ")
                        else:
                            print(" ",end="  ")    
                    elif i == 1 or i ==5:
                        if j == 0 or j ==3:
                            print("K",end="  ")    
                        else:
                            print(" ",end="  ")  
                    elif i == 2 or i ==4:
                        if j == 0 or j ==2:
                            print("K",end="  ")    
                        else:
                            print(" ",end="  ") 
                    elif i == 3 :
                        if j == 0 or j ==1:
                            print("K",end="  ")    
                        else:
                            print(" ",end="  ")           
                print(" ")
        print("\n") 

    # IT prints L
    elif alpha1 =="L":    
            for i in range (6):
                for j in range(5):
                    if i == 5:
                        print("L", end="  ")
                    else:
                        if j == 0:
                            print("L",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
            print("\n")  

    # it prints M     
    elif alpha1 =="M":
        for i in range (6):
                for j in range(5):
                    if i == 1 :
                        if j == 2:
                            print(" ", end="  ")
                        else:
                            print("M", end="  ")
                    elif i == 2:
                        if j == 2 or j== 0 or j == 4:
                            print("M", end="  ")
                        else:
                            print(" ", end="  ")            
                    else:
                        if j == 0 or j ==4:
                            print("M",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
        print("\n") 

    # it prints   N     
    elif alpha1 =="N":
        for i in range (5):
                for j in range(5):
                    if i == 1 :
                        if j == 2 or j == 3:
                            print(" ", end="  ")
                        else:
                            print("N", end="  ")
                    elif i == 2:
                        if j == 2 or j== 0 :
                            print("N", end="  ")
                        else:
                            print(" ", end="  ")   
                    elif i== 3:
                        if j == 1 or j == 2 :
                            print(" ", end="  ")
                        else:
                            print("N", end="  ")                  
                    else:
                        if j == 0 or j ==4:
                            print("N",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
        print("\n") 

    # iT prints o
    elif alpha1 =="O":       
            for i in range(5):
                if i == 1 or i == 2 or i== 3:
                    for j in range(4):
                        if j == 1 or j == 2:
                            print(" ",end="  ") 
                        else:
                            print("O",end="  ")    
                else:
                    for j in range(4):
                        print('O', end="  ")
            

                print(" ")
            print("\n")

    # it prints P     
    elif alpha1 =="P":
        for i in range(7):
                for j in range(5):
                    if i == 1 or i == 2 :
                            if j == 1 or j == 2 or j == 3:
                                print(" ",end="  ") 
                            else:
                                print("P",end="  ")    
                    elif i == 0 or i ==3:        
                        print("P",end="  ")

                    else:
                        if j ==0:
                            print("P",end="  ")
                        else:
                            print(" ",end="  ") 


                print(" ")
        print("\n")

    # it prints Q     
    elif alpha1 =="Q":
            for i in range(7):
                for j in range(5):
                    if i in (1,2) :
                            if j in (1,2,3):
                                print(" ",end="  ") 
                            else:
                                print("Q",end="  ") 

                    elif i in (0,3,4):        
                        print("Q",end="  ")

                    elif i == 5:
                        if j == 2 or j == 3:
                            print("Q",end="  ")
                        else:
                            print(" ",end="  ")    

                    elif i == 6:
                        if j == 3  or j == 4:
                            print("Q",end="  ") 
                        else:
                            print(" ",end="  ") 
                print(" ")
            print("\n")        

    # iT prints R    
    elif alpha1 =="R":    
            for i in range(7):
                for j in range(5):
                    if i == 1 or i == 2 :
                            if j == 1 or j == 2 or j == 3:
                                print(" ",end="  ") 
                            else:
                                print("R",end="  ")    
                    elif i == 0 or i ==3:        
                    
                        print("R",end="  ")
                    elif i == 4:
                        if j == 0 or j == 1 or j == 2:
                            print("R",end="  ")

                    elif i == 5:
                        if j == 1  or j == 4:
                            print(" ",end="  ") 
                        else:
                            print("R",end="  ") 
                    elif i == 6:   
                        if j == 1 or j == 2 :
                            print(" ",end="  ") 
                        else:
                            print("R",end="  ") 

                print(" ")
            print("\n")

    # it prints S     
    elif alpha1 =="S":
        pass
    
    # it prints T        
    elif alpha1 =="T":
        pass

    # it prints U     
    elif alpha1 =="U":
        for i in range (6):
                for j in range(5):
                    if i == 5:
                        print("U", end="  ")
                    else:
                        if j == 0 or j == 4:
                            print("U",end="  ")    
                        else:
                            print(" ",end="  ")     
                print(" ")
        print("\n")
    
    # it prints V     
    elif alpha1 =="V":
        pass
    
    # it prints W    
    elif alpha1 =="W":
        pass
    
    # it prints X     
    elif alpha1 =="X":
        pass
    
    # it prints Y     
    elif alpha1 =="Y":
        pass

    # it prints Z    
    elif alpha1 =="Z":
        pass



name = input("What is your Name\t").upper()
n_length = len(name)


for i in range(n_length):
    a = name[i]
    alphabate(a)

exit = input("Press enter to exit: ")   
  



