from Tkinter import *
import PIL
from PIL import ImageTk
import matplotlib.pyplot as plt
import os.path
import math
root = Tk()

# A slider to set the diameter of created circles
diameter = IntVar()
diaSlider = Scale(root,variable=diameter, from_=1, to=300,
                  orient=HORIZONTAL, label='Diameter:')
diaSlider.set(150)
diaSlider.pack()

#Create a check box window for colors
col = StringVar()
Radiobutton(root, text="Blue", variable=col, value='#0000cd').pack(anchor=W)
Radiobutton(root, text="Red", variable=col, value='#ff4500').pack(anchor=W)
Radiobutton(root, text="Green", variable=col, value='#228b22').pack(anchor=W)

#Try to make an option for balls to bounce around, (WIP)
def animate():
    velocity_x = speed_intvar.get() * math.cos(direction)
    velocity_y = speed_intvar.get() * math.sin(direction)
    canvas.move(circle_item, velocity_x, velocity_y)
    x1, y1, x2, y2 = canvas.coords(circle_item)
    global direction

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=800, width=1600, relief=RAISED, bg='white')
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