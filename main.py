from tkinter import *

root = Tk()
root.title("Chat")
root.geometry("600x400")

menu = Menu(root)
root.config(menu=menu)

label = Label(root, text="Chat", font=("Arial", 64), foreground="cyan")

root.mainloop()