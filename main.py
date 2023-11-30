import tkinter as tk
from PIL import Image, ImageTk

def clear_frame(frame):
    for i in frame.winfo_children():
        i.destroy()
    frame.pack_forget()

class Scene:
    def __init__(self, root, image_path, text_path, commands, options, previous_scenes):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.image_path = image_path
        self.text_path = text_path
        self.commands = commands
        self.options = options
        self.previous_scenes = previous_scenes
    
    def draw_scene(self):
        # Clear everything from previous scene
        if self != Intro:
            for i in self.previous_scenes:
                exec(f'clear_frame({i}.mainframe)')
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
        index = 1
        for i in self.commands, self.options:
            exec(f"button{index} = tk.Button(self.mainframe, text=f'{self.options[index-1]}', command=lambda: exec(f'{self.commands[index-1]}'))")
            exec(f"button{index}.grid(row=2, column={index-1})")
            if (index+1) <= len(self.commands):
                index += 1
    

root = tk.Tk()

# Level 0
Intro = Scene(root, 'images\_tent.jpg', "scenes_text\Intro.txt", ["scene1a.draw_scene()", "scene1b.draw_scene()"], ["Gå ut fra telt", "Sove mer"], None)

# Level 1
scene1a = Scene(root, 'images\warchief.jpg', "scenes_text\scene_1a.txt", ["", ""], ["Alver? Har?! Samle troppen!", "Alver? Kanskje, vi kan bli enige?"], ['scene1b','Intro'])
scene1b = Scene(root, 'images\_tent.jpg', "scenes_text\scene_1b.txt", ["scene1a.draw_scene()", "scene2c.draw_scene()"], ["Våkn opp og gå ut fra telt", "Sove mer"], ['Intro'])

# Level 2
scene2c = Scene(root, 'images\dead.jpg', "scenes_text\dead_2b.txt", [], [], ['scene1b'])


# Launch level 0
Intro.draw_scene()

# Launch gameloop
root.mainloop()

