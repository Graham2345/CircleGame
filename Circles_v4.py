from Tkinter import *
import PIL
from PIL import ImageTk
import matplotlib.pyplot as plt
import os.path
root = Tk()

# A slider to set the diameter of created circles
diameter = IntVar()
diaSlider = Scale(root,variable=diameter, from_=1, to=300,
                  orient=HORIZONTAL, label='Diameter:')
diaSlider.set(150)
diaSlider.pack()

#Create a check box window for colors
#master = Tk()
col = StringVar()
Radiobutton(root, text="Blue", variable=col, value='blue').pack(anchor=W)
Radiobutton(root, text="Red", variable=col, value='red').pack(anchor=W)
Radiobutton(root, text="Green", variable=col, value='green').pack(anchor=W)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=800, width=800, relief=RAISED, bg='white')
canvas.pack()

# Define stamp as an event that makes a circle
def click(event):
    d = diameter.get()
    x = event.x
    y = event.y
    oval = canvas.create_oval(x-d, y-d, x+d, y+d, outline='#000000', fill= (col.get()))
canvas.bind('<ButtonPress-1>', click)

# Enter event loop
root.mainloop()