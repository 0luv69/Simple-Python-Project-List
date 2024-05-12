from time import strftime as time00
import tkinter as tk

#windows
windows= tk.Tk(className=("Great Me"))
windows.title("Great me")
windows.geometry("650x230")
windows.configure(bg='#FAF1E4')
windows.resizable(False,False)
# windows['background']='yellow' # it is same as upper code its also gonna change color

# the title
title= tk.Label(master=windows,text="This program is devoted to Great the user according to time",font="TIMES 18 underline bold").pack(side="top",pady="18")

# greet you
greetyou=tk.StringVar()
text=tk.Label(master=windows,text="greet you sir",textvariable= greetyou,font="Times 40 italic bold",background="#279EFF").pack(pady="50")

current_hour1 =time00 ('%H')
current_hour = int(current_hour1)

if current_hour >= 5 and current_hour < 12 :
    greetyou.set("Good mor1ning sir")

elif current_hour >= 12 and current_hour< 18:  
    greetyou.set("Good afternoon sir")
         
elif current_hour >= 18 and current_hour < 19: 
    greetyou.set("Good Evening sir")  
else:
    greetyou.set("Good Night sir") 
#run
windows.mainloop()

















