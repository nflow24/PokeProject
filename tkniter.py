from tkinter import *
from PIL import *
import requests
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain widgets

window = Tk() #instantiate an instance of a window
window.geometry("200x200") #window size
window.title("PokeProject") #changes title of window
photo = PhotoImage(file='sprites/pikachu.png')
header = Label(window,
               text="Pokemon",
               font=("Arial", 30, "bold"),
               fg="white",
               bg="black",
               relief="raised",
               bd=10,
               padx=10,
               pady=10,
               image=photo,
               compound=BOTTOM)
header.pack()
# header.place(x=100, y=100)
"""to change feather icon next to window title:
    1) import photo into directory
    2) icon = PhotoImage(file='logo.png')) #changes image type to PhotoImage
    3) window.iconphoto(True, icon)
"""
window.config(background="#66e7a9")
window.mainloop() #place window on computer screen, listen for events