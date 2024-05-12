import pyttsx3
import tkinter as tk
from ttkbootstrap import ttk

def speaks():
    word=answer_inputs.get()
    speak = pyttsx3.init()
    speak.say(word)
    speak.runAndWait()
    speak.stop()
    
# displays
win = tk.Tk()
win.geometry("640x500")
win["bg"]="#99627A"
# # warning
# Warning_r= tk.StringVar()
# warn=tk.Label(master=win,background="red",textvariable=Warning_r).pack()
inputframe=tk.Label(master=win)
# questions
q= tk.Label(master=inputframe, text="Enter your sentence to read:",font="Times 30 bold").pack(pady=(20,20))

#answer
answer_inputs= tk.StringVar()
answer=tk.Entry(master=inputframe,font="Times 14",textvariable=answer_inputs).pack(ipadx=100,ipady=12)

# summit
tk.Button(master=inputframe,text="Submmit",command=speaks,background="#F266AB",font="times 13").pack(pady=(30,5),ipady=(20),ipadx=(30))


#runss
inputframe.pack(pady=(40,0),ipady=(40))
win.mainloop()
