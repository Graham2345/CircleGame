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

# Bind a function to the left mouse button down event.
def stamp(event):
    Canvas.create_image(event.x,event.y,image=tkimg)
    print reduceSlider.get()
Canvas.bind('<ButtonPress-1>', stamp)

# A canvas for mouse events and image drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='white')
canvas.pack()

# Enter event loop
root.mainloop() 