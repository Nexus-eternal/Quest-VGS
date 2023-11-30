import tkinter as tk
from PIL import Image, ImageTk

def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

class Scene:
    def __init__(self, root, image_path, text_path, to_scene_1, to_scene_2):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.mainframe.pack()
        self.image_path = image_path
        self.text_path = text_path
        self.to_scene_1 = to_scene_1
        self.to_scene_2 = to_scene_2
    
    def draw_scene(self):
        #Clear everything from previous scene
        clear_frame(self.mainframe)

        # Unpacking image and placing it
        image = Image.open(self.image_path)
        tk_image = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.mainframe)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image
        self.image_label.grid(row=0, column=0, columnspan=2)

        #Unpacking text
        file = open("scenes_text\Into.txt", "r", encoding="utf-8" )
        content = file.read()
        print(content)

        text_label = tk.Label(self.mainframe, text=content)
        text_label.grid(row=1, column=0, columnspan=2)
