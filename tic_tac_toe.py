import random
import os
import numpy as np

po_player1=[]
po_palyer2=[]
positions = [1,2,3,4,5,6,7,8,9]

win_sleep_structure = np.array([[1,2,3],[4,5,6],[7,8,9]])
win_stand_structure = np.array([[1,4,7],[2,5,8],[3,6,9]])
win_cross_structure = np.array([[1,5,9],[3,5,7]])

def ask_user_position(player):
    while True:
            user_position =int(input(f"\n\nChoose a positions for {player}, from (1-9) where you want to address yourself:\t"))
            if user_position in positions:
                pops(user_position)
                return user_position 
            else:
                print("Sorry may be this position is allready occupied or wrong number input\n\n\t\tTry Again")
                
def brain(top,who):
     if len(top)>=3:
        s1=s2=s3=s4=s5=s6=s7=s8=s9=0
        for jokk in top:
            if jokk ==1:s1= jokk
            if jokk ==2:s2= jokk
            if jokk ==3:s3= jokk
            if jokk ==4:s4= jokk
            if jokk ==5:s5= jokk
            if jokk ==6:s6= jokk
            if jokk ==7:s7= jokk
            if jokk ==8:s8= jokk
            if jokk ==9:s9= jokk
        sleep_structure = np.array([[s1,s2,s3],[s4,s5,s6],[s7,s8,s9]])
        stand_structure = np.array([[s1,s4,s7],[s2,s5,s8],[s3,s6,s9]])
        cross_structure = np.array([[s1,s5,s9],[s3,s5,s7]])
        
        for dog in range(3):
            if np.array_equal(win_sleep_structure[dog],sleep_structure[dog]):
               
               return who
            elif np.array_equal(win_stand_structure[dog],stand_structure[dog]):
               
               return who
            
        for dogs in range(2):
            if np.array_equal(win_cross_structure[dogs],cross_structure[dogs]):
                 
               return who
         
def pops(user_position1):
    locateds = positions.index(user_position1)
    positions.pop(locateds)

def print_format(player1symbol,player2symbol):
    os.system("cls")   # to clear the screen

    # adding "___" according to user_word count
    dash = "___________"
    for no in (list(player1symbol)):
        dash = dash + "_"
    p1=p2=p3=p4=p5=p6=p7=p8=p9=" " #to fill the empty sopt
    
    # to fill the Player1 and Player2 Symbol
    for jok in po_player1:
            if jok ==1:p1= player1symbol
            if jok ==2:p2= player1symbol
            if jok ==3:p3= player1symbol
            if jok ==4:p4= player1symbol
            if jok ==5:p5= player1symbol
            if jok ==6:p6= player1symbol
            if jok ==7:p7= player1symbol
            if jok ==8:p8= player1symbol
            if jok ==9:p9= player1symbol
    for jock in po_palyer2:
            if jock ==1:p1= player2symbol
            if jock ==2:p2= player2symbol
            if jock ==3:p3= player2symbol
            if jock ==4:p4= player2symbol
            if jock ==5:p5= player2symbol
            if jock ==6:p6= player2symbol
            if jock ==7:p7= player2symbol
            if jock ==8:p8= player2symbol
            if jock ==9:p9= player2symbol
    
    structure_to_print=f"""\n {p1} | {p2} | {p3}\n{dash}\n\n {p4} | {p5} | {p6}\n{dash}\n\n {p7} | {p8} | {p9}"""
    print(structure_to_print)
      
    #Brain
    player_1_call=brain(po_player1,player1symbol)
    player_2_call=brain(po_palyer2,player2symbol)
   
    if player_1_call == player1symbol:
        print(f"\n\n{player1symbol} has achived win")
        return "P1"
    if player_2_call == player2symbol:
        print(f"\n\n{player2symbol} has achived win")
        return "P2"
    else:
        return"fuck"
    
chooce = int(input("\n\n\t\t1) With Computer  \t\t\t2) With ur Friend\nEnter whom you want to play with:\t")   )  
print("  1| 2 | 3")
print("___________\n")
print("  4| 5 | 6")
print("___________\n")
print("  7| 8 | 9")

won = 0
#computer choice
if chooce == 1:
    player1symbol = input("\n\nChoose a letter like(x,y,w):\t")
    tho = 1
    for i in range(5): 
        user_position=ask_user_position("PLayer 1")
        po_player1.append(user_position)
        if po_player1[0] != 5 and tho == 1:
            computer_choice1 = 5
            pops(computer_choice1)
            po_palyer2.append(computer_choice1)
            tho -=1
        
        elif len(positions)!=0:
            computer_choice= random.choice(positions)
            pops(computer_choice)
            po_palyer2.append(computer_choice)
        
        to_stop_or_not=print_format(player1symbol,"Comp")    
        
        if to_stop_or_not.upper() == "P2":
            print(f"so computer won")
            won+=1
            break
        elif to_stop_or_not.upper() == "P1":
            print(f"You won")
            won+=1
            break
    if won == 0:    
        print("The Match is draw now")    

# two player choice
elif chooce == 2:
    player1symbol = input("\n\nChoose Player 1 symbol, like(x,y,w):\t")
    player2symbol = input("\n\nChoose Player 2 symbol, like(x,y,w):\t")
    
    for i in range(5): 
        user_position_1=ask_user_position("PLayer 1")
        po_player1.append(user_position_1)
        to_stop_or_not=print_format(player1symbol,player2symbol)
        if to_stop_or_not.upper() == "P2":
            print(f"Player Two won!!!!!!!!!!!!!!!!!!")
            break
        elif to_stop_or_not.upper() == "P1":
            print(f"Player One won!!!!!!!!!!!!!!!!!!")
            won+=1
            break

        if i == 4:
            won+=1
            break

        user_position_2=ask_user_position("PLayer 2")
        po_palyer2.append(user_position_2)    
        to_stop_or_not=print_format(player1symbol,player2symbol)    
        if to_stop_or_not.upper() == "P2":
            print(f"Player Two won!!!!!!!!!!!!!!!!!!")
            won+=1
            break
        elif to_stop_or_not.upper() == "P1":
            print(f"Player One won!!!!!!!!!!!!!!!!!!")
            won+=1
            break
    if won == 0:    
        print("The Match is draw now") 
     
