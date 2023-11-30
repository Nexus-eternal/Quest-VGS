import tkinter as tk
from scenes import *


root = tk.Tk()

scene1 = Scene(root, "images\warchief.jpg", "ABOBA", None, None)
scene1.draw_scene()

root.mainloop()

