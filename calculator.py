print("This is calculator created by Rujal Baniya")
p ="Y"
while p == "Y": 
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter Second number"))
    opp = input("WHat you want to do \n if you want to \n add = a \n sub = s \n mul = m \n div = d \n >>>>>").upper()
    if opp == "A":
                sum = num1+num2
                print(" The add of " , num1 , " and ", num2 , " is " , sum)

    elif opp == "S":
                sub = num1 - num2
                print(" The subtract of " , num1 , " and ", num2 , " is " , sub)  
    elif opp == "M":
                mul = num1 * num2
                print(" The multiple of " , num1 ," and ", num2 ," is " , mul) 
    elif opp == "D":
                div = num1 / num2
                print(" The subtract of " , num1 ," and ", num2 ," is " , div) 
    else:
                print("Enter only the letter according to instructions given above")

    p = input("Do you want to continue then write Y else N\t").upper()
a = input("press Enter key to exit")