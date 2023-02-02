from tkinter import *

root = Tk()
root.title("Chat")
root.geometry("600x400")

def con():
    text.insert(1.0, "\n Hello World.")

menu = Menu(root, tearoff=0)
chatmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Chat", menu=chatmenu)
chatmenu.add_command(label="Connect", command=con)

root.config(menu=menu)

text = Text(root)

label = Label(root, text="Chat", font=("Arial", 64), foreground="cyan")
label.pack()
text.pack()
root.mainloop()
