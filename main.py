import tkinter as tk
from PIL import Image, ImageTk

# Counters
Elves = 36
Orcs = 50
Hatered = 0
Friendship = 0
Sleeping = 1
counters = [Elves, Orcs, Hatered, Friendship, Sleeping]


def clear_frame(frame):
    for i in frame.winfo_children():
        i.destroy()
    frame.pack_forget()

class Scene:
    def __init__(self, root, image_path, text_path, commands, options, previous_scenes, triggers):
        self.root = root
        self.mainframe = tk.Frame(self.root)
        self.image_path = image_path
        self.text_path = text_path
        self.commands = commands
        self.options = options
        self.previous_scenes = previous_scenes
        self.triggers = triggers
    
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
        for i in self.commands, self.options, self.triggers:
            exec(f"button{index} = tk.Button(self.mainframe, text=f'{self.options[index-1]}', command=lambda: exec(f'{self.commands[index-1]}'))")
            exec(f"button{index}.grid(row=2, column={index-1})")
            exec(f"{self.triggers[index-1]}")
            if (index+1) <= len(self.commands):
                index += 1
        
        # Triggers
        for i in self.triggers:
            exec(f'{i}')
        
    def launch_scene(self):
        # Counters checking
        if Sleeping == 5:
            scene2c.draw_scene()
        
        # Main function
        else:
            self.draw_scene()
    




    

root = tk.Tk()

# Level 0
Intro = Scene(root, 'images\_tent.jpg', "scenes_text\Intro.txt", ["scene1a.launch_scene()", "scene1b.launch_scene()"], ["Gå ut fra telt", "Sove mer"], [], ['',''])

# Level 1
scene1a = Scene(root, 'images\warchief.jpg', "scenes_text\scene_1a.txt", ["scene2a.launch_scene()", "scene2b.launch_scene()"], ["Alver? Har?! Samle troppen!", "Alver? Kanskje, vi kan bli enige?"], ['scene1b','Intro'], ['Hatered += 1','Friendship += 1'])
scene1b = Scene(root, 'images\_tent.jpg', "scenes_text\scene_1b.txt", ["scene1a.launch_scene()", "scene2c.launch_scene()"], ["Våkn opp og gå ut fra telt", "Sove mer"], ['Intro'], ['','Sleeping += 1'])

# Level 2
scene2a = Scene(root, 'images\_ranger.jpg', "scenes_text\scene_2a.txt", ["scene3a.launch_scene()", "scene3b.launch_scene()"], ["Ha, grisseøret søppel! Gi opp og...", "Vi vil snakke med lederene dine!"], ['scene1a'], ['',''])
scene2b = Scene(root, 'images\druid.jpg', "scenes_text\scene_2b.txt", ["scene3c.launch_scene()", "scene3c.launch_scene()"], ["Selvfølgelig! Da hvor mye øl trenger dere?", "Glad å hjelpe deg! Så hva egentlig trenger dere?"], ['scene1a'], ['',''])
scene2c = Scene(root, 'images\dead.jpg', "scenes_text\dead_2c.txt", [], [], ['scene1b'], [])

# Level 3
# Ranger line
scene3a = Scene(root, 'images\dead.jpg', "scenes_text\dead_3a.txt", [], [], ['scene2a', 'scene3b'], [])
scene3b = Scene(root, 'images\_ranger.jpg', "scenes_text\scene_3b.txt", ["scene3a.launch_scene()", "scene4a.launch_scene()"], ["Ha, hvis du virkelig vil være alene med meg...", "Selvfølgelig! Vi har mye å snakke om"], ['scene2a'], ['',''])
# Druid line
scene3c = Scene(root, 'images\druid.jpg', "scenes_text\scene_3c.txt", ["scene3d.launch_scene()","scene4a.launch_scene()"], ["Du vet, jeg vil ikke kom til leiren. Men hvis DU går til meg...", "Ja, hvorfor ikke? Da vil du ta meg gjennom?"], ['scene2b'], ['',''])
scene3d = Scene(root, 'images\dead.jpg', "scenes_text\dead_3d.txt", [], [], ['scene3c', 'scene3b'], [])

# Level 4
# Camp line
scene4a = Scene(root, 'images\camp.jpg', "scenes_text\scene_4a.txt", ["scene5a_1.launch_scene()"], ["Kom inn etter hun"], ['scene3c', 'scene3b'], [])

# Level 5
scene5a_1 = Scene(root, 'images\meeting.jpg', "scenes_text\scene_5a_1.txt", ["scene5a_2.launch_scene()"], ["Neste"], ['scene4a'], [])
scene5a_2 = Scene(root, 'images\meeting.jpg', "scenes_text\scene_5a_2.txt", ["scene5a_3.launch_scene()"], ["Neste"], ['scene5a_1'], [])
scene5a_3 = Scene(root, 'images\meeting.jpg', "scenes_text\scene_5a_3.txt", ["scene5a_4.launch_scene()"], ["Neste"], ['scene5a_2'], [])
scene5a_4 = Scene(root, 'images\meeting.jpg', "scenes_text\scene_5a_4.txt", ["scene5a_5.launch_scene()"], ["Neste"], ['scene5a_3'], [])
scene5a_5 = Scene(root, 'images\meeting.jpg', "scenes_text\scene_5a_5.txt", ["scene_6b.launch_scene()", "scene_6b.launch_scene()"], ["Enig", "Pffff, nei, grisseøret!"], ['scene5a_4'], [])

# Level 6
Scene_6a = Scene(root, 'images\dead.jpg', "scenes_text\win_6a.txt", [], [], ['scene5a_5'], [])
Scene_6b = Scene(root, 'images\dead.jpg', "scenes_text\dead_6b.txt", [], [], ['scene5a_5'], [])


# Launch level 0
Intro.draw_scene()

# Launch gameloop
root.mainloop()

