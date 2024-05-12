import pyautogui
import time

import tkinter as tk
from ttkbootstrap import ttk

def adds(word,num,i):
    words =(list(word))
    try:
        words.insert(int(num), f" {i+1} ") 
        return_value = "".join(words)
        return return_value

    except:
        pass

def when_pressed():
    display.geometry("1000x500")
    what_is_word =theword.get()
    print(what_is_word)
    # qus.configure(text="\tWhere to add number f= First,l= Last,n= No, number_after_what_letter---[f/l/n]:\t")
    qus['text']=("\tWhere to add number f= First,l= Last,n= No, number_after_what_letter---[f/l/n]:\t")



    


# create windows/display
display = tk.Tk(className="Automatic writter")
display.geometry("680x500")
display['bg']='#E8D5C4'

#title
Lg=ttk.Label(master=display,text="----__To write Automatically for provided time__----",font="Times 18 italic bold",background="#ACBCFF").pack(pady=20)

#Take inputs
## inputframe
input_frame=ttk.Label(master=display)


##Ask question
qus= ttk.Label(master=input_frame,text="\tEnter what is word that you want to enter\t",background="#62CDFF",font="Times 15")
qus.pack(pady=(30,5))


## take answer
theword= tk.StringVar()
what_is_word00= ttk.Entry(master=input_frame,textvariable=theword,font="Times 20")
what_is_word00.pack(side="left",padx=(80,0))

## button
buttonn= ttk.Button(master=input_frame,text="Summit",command=when_pressed).pack(side="left",ipadx=20,ipady=9)



input_frame.pack(ipady=(50),pady=(70,0))
#run
display.mainloop()

        



what_is_word =1 #input("\nEnter what is word that you want to enter:\t")
addnum =2 #input("\n\nwhere to add number f= First,l= Last,n= No, number_after_what_letter---[f/l/n]:\t")
whats = 2#input(f"\nThis is preview\n\t\t{(adds(what_is_word,(addnum),(1)))}\n\t[y/n]:")
if whats.upper() =="Y":
    
    total_time = int(input("\n\nEnter how many times to print the inputs:\t"))
    time.sleep(10)
    try:
        int(addnum)
        print(total_time)
        for i in range(total_time):
            what_is_word2 = adds(what_is_word,int(addnum),(i+1))
            pyautogui.typewrite(f"{what_is_word2}")
            pyautogui.press("ENTER") 
    except:
        print("",end="")

    if addnum.upper() =="F":
        
        for i in range(total_time):
            pyautogui.typewrite(f"{i+1} {what_is_word}")
            pyautogui.press("ENTER")

    elif addnum.upper() =="L":
        
        for i in range(total_time):
            pyautogui.typewrite(f"{what_is_word} {i+1}")
            pyautogui.press("ENTER")

    elif addnum.upper() =="N":
        for i in range(total_time):
            pyautogui.typewrite(f"{what_is_word}")
            pyautogui.press("ENTER")        

            
     
