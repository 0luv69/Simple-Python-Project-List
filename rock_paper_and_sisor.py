from random import randint as random_num

def check(human,comp):
    if   human == comp :
        print("Hey its draw \n") 
        return "DRAW"

    elif human=="PAPER" and comp =="ROCK": 
        print("You Won\n") 
        return "HUMAN"

    elif human=="ROCK" and comp =="SISOR": 
        print("You Won\n") 
        return "HUMAN"

    elif human=="SISOR" and comp =="PAPER": 
        print("You Won\n") 
        return "HUMAN"
    elif human=="ROCK" and comp =="PAPER": 
        print("I won \n")
        return "COMP"
    elif human=="SISOR" and comp =="ROCK": 
        print("I won \n")
        return "COMP"
    elif human=="PAPER" and comp =="SISOR": 
        print("I won \n")
        return "COMP"
draw_mark = 0    
com_mark = 0
human_mark = 0
question = 0 
Input = 3
while Input!= 4:
        print("Lets play The Game")
        cases = ["PAPER","ROCK","SISOR"] 
        print("Choose one\n1) Paper\t2)Rock\t\t3)Sisor\n\n\tAnd \"4\" to Quite\n")
         
        # Asking user to enter the number
        Input =int(input("Enter a number among 1,2 or 3\t"))    
        if Input <= 3 and Input >=1:    
            input2 = (Input - 1)
            print(f"OK you choosed {(cases[input2]).title()}")
            human = (cases[input2])
            
            # Making computer to choose among sisor paper and rock
            random_number= random_num(0,2)
            print(f"And i choose as {(cases[random_number]).title()}\n")
            computer = (cases[random_number])
            result = check(human,computer)
            
            #counting the scores
            question = question + 1
            if result == "HUMAN":
                human_mark = human_mark + 1

            elif result == "DRAW":
                
                draw_mark = draw_mark+1

            else:
                com_mark = com_mark + 1 

        elif Input==4:
            print("Quiting the program\n\t\tBye")

        else:    
            print("\nSorry, You have entered wrong input \n\t\tTry again\n\n")

print(f"\nThanks for playing the Game\nTotal Game played :{question}\nYour Total win is :{human_mark}\nMy Total win is:{com_mark} \nAnd total draw match is:{draw_mark}")  
input("Press Enter to exit")                             