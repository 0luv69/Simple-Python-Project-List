# iT prints R
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

# it prints U
print("\n")
for i in range(6):
    for j in range(5):
        if i == 5:
            print("U",end="  ")        
        else:
            if j == 1 or j == 2 or j ==3:
                print(" ",end="  ")  
            else:
                print("U",end="  ")
    print("")  

print("\n")


# it prints J
for i in range(5):
    for j in range (5):
        if i == 0:
            print("J", end="  ")
        elif i ==1 or i == 2:
            if j == 0 or j ==1:
                print(" ", end= "  ")
            elif j == 3:
                print("J", end = "  ")
        elif i == 3:
            if j == 0 or j == 2:
                print("J", end="  ")
            else:
                print(" ", end= "  ")
        elif i == 4:
            if j == 1 or j == 2:
                print("J", end="  ")  
            else:
                print(" ", end= "  ")                  
    print("")

print("\n")

# it prints A

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

# IT prints L

for i in range (5):
    for j in range(5):
        if i == 4:
            print("L", end="  ")
        else:
            if j == 0:
                print("L",end="  ")    
            else:
                print(" ",end="  ")     
    print(" ")
print("\n")    


