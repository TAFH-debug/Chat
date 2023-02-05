from tkinter import *

class Channel(Button):
    def on_click(self):
        pass
    
    def __init__(self, master, text):
        super().__init__(master, text=text, activebackground="#ECF87F", font=("Helvetica", 16), anchor="w")
        self.config(borderwidth=0, bg="#81B622")


class Message(Frame):
    
    def __init__(self, master, author, text):
        super().__init__(master, bg="#466818")
        self.author_l = Label(self, text=author + ":", font=("Helvetica", 14, 'bold'), anchor="w", fg="white").inherit_bg()
        self.text_l = Label(self, text=text, font=("Helvetica", 12), anchor="w", fg="white").inherit_bg()
    
    def pack(self, *args, **kwargs):
        super().pack(*args, **kwargs)
        self.author_l.pack(side=LEFT,fill=X, padx=15)
        self.text_l.pack(side=LEFT, fill=X)

