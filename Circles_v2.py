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

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.pack()

# Define stamp as an event that makes a circle
def click(event):
    x = event.x
    y = event.y
    oval = canvas.create_oval(x-6, y-6, x+6, y+6, outline='#000000', fill='#00FFFF')
canvas.bind('<ButtonPress-1>', click)

# Enter event loop
root.mainloop()