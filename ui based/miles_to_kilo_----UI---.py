import tkinter as tk
# from tkinter import ttk
i=0
def convetrs():
    inputs=(entryint.get())
    miles= inputs*1.61
    output_string.set(f"{miles} Km")

# windows
window = tk.Tk()
window.title("Conveter")
window.geometry("400x300")


#INside content
#Title
title_label= tk.Label(master=window, text='Miles to Kilometer',font="calibri 30 bold").pack()

#input field
input_frame= tk.Label(master=window)
entryint= tk.IntVar()
entry= tk.Entry(master=input_frame,textvariable=entryint).pack(side='left')
button= tk.Button(master=input_frame,text="calculate",command=convetrs)

button.pack(side='left')
input_frame.pack(pady=20)


#output
output_string=tk.StringVar()
output_label= tk.Label(master=window,text="Output",font="calibri 26 bold",textvariable=output_string).pack()



# run
window.mainloop()