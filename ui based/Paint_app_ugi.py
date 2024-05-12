import tkinter as tj
from ttkbootstrap import ttk

# open the window
windows= tj.Tk()
windows.title("Paint tools")
windows.geometry("800x600")
# windows.configure(bg="red")
windows["bg"]="red"



def change_color(event):
    global colors
    colors= selcet_var.get()


#00##   mainwork
#title
tj.Label(windows,text="Paint App",font="Times 50 underline bold").pack()

#clolor choose
colors= "red"
all_colors=("red","blue","pink","yellow","black","White")
selcet_var=tj.StringVar(value=all_colors[0])
selcet=ttk.Combobox(windows,textvariable=selcet_var)
selcet["value"]=all_colors
selcet.pack()
selcet.bind("<<ComboboxSelected>>",change_color)


#canvas
canvas0=tj.Canvas(windows,bg="Yellow",height=450,width=750)
draw_box=canvas0.create_rectangle((3,5,748,448),width=5)
canvas0.tag_lower(draw_box)
canvas0.pack()

def power(event):
    x=event.x
    y=event.y
    # print(f"X:  {x}  ,Y:   {y}")
    if brushsize>4:
        ratio=brushsize+2
    else:
        ratio=0
    if x<=8+brushsize or x>=744-brushsize or y>=444-brushsize or y<=8+brushsize:
        pass
    else:    
        canvas0.create_oval((x-brushsize,y-brushsize,x+brushsize,y+brushsize),fill=colors,width=0)

def adjust_size(ent):
    global brushsize
    if ent.delta >1 and brushsize>=2:
            brushsize=brushsize-1
    elif ent.delta <=0 and brushsize<50:
            brushsize=brushsize+1    

# adding event/bind
brushsize=4
canvas0.bind("<B1-Motion>",power)
canvas0.bind("<MouseWheel>",adjust_size)


# run the windos
windows.mainloop()