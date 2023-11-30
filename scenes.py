import tkinter as tk

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()
