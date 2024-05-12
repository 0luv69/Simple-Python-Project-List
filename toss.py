import random
a=1
while a==1:
    random_num= random.randint(0,1)

    if random_num==1:
        print("Its head")
    else:
        print("cool, its tail")    

    inputs=input("press enter to exit:")   
    if inputs=="":
        a=1
    else:
        a=0    
