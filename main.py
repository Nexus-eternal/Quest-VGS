import tkinter as tk
from PIL import Image, ImageTk

def clear_frame(frame):
    for i in frame.winfo_children():
        i.destroy()
    frame.pack_forget()

class Scene:
    def __init__(self, root, image_path, text_path, command_1, command_2, option_1, option_2, previous_scene):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.image_path = image_path
        self.text_path = text_path
        self.command_1 = command_1
        self.command_2 = command_2
        self.option_1 = option_1
        self.option_2 = option_2
        self.previous_scene = previous_scene
    
    def draw_scene(self):
        # Clear everything from previous scene
        if self != Intro:
            clear_frame(self.previous_scene.mainframe)
        self.mainframe.pack()

        # Unpacking image and placing it
        image = Image.open(self.image_path)
        tk_image = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.mainframe)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image
        self.image_label.grid(row=0, column=0, columnspan=2)

        # Unpacking text
        file = open(self.text_path, "r", encoding="utf-8" )
        content = file.read()

        text_label = tk.Label(self.mainframe, text=content)
        text_label.grid(row=1, column=0, columnspan=2)

        # Buttons
        button1 = tk.Button(self.mainframe, text=f"{self.option_1}", command=lambda: exec(f'{self.command_1}'))
        button1.grid(row=2, column=0)
        button2 = tk.Button(self.mainframe, text=f"{self.option_2}", command=lambda: exec(f'{self.command_2}'))
        button2.grid(row=2, column=1)

root = tk.Tk()

Intro = Scene(root, 'images\_tent.jpg', "scenes_text\Intro.txt", "scene1a.draw_scene()", "scene1b.draw_scene()", "Gå ut fra telt", "Sove mer", None)
scene1a = Scene(root, 'images\warchief.jpg', "scenes_text\Intro.txt", "", "", "AAAAAAA", "BBBBBB", Intro)
scene1b = Scene(root, 'images\_tent.jpg', "scenes_text\scene1b.txt", "", "scene1b.draw_scene()", "AAAAAAA", "Sove mer", Intro)
Intro.draw_scene()


root.mainloop()

