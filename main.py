from tkinter import *
from cls import *
from net import *
import util

root = Tk()
root.title("Chat")
root.geometry("1000x800")

nickname = ""

def con():
    con_lbl1.pack()
    con_ip.pack()
    con_lbl2.pack()
    con_nickname.pack()
    con_btn.pack()

def crt():
    crt_lbl1.pack()
    crt_chn.pack()
    crt_lbl2.pack()
    crt_nickname.pack()
    crt_btn.pack()

def con_proc(ip, nick):
    con_lbl1.pack_forget()
    con_ip.pack_forget()
    con_lbl2.pack_forget()
    con_nickname.pack_forget()
    con_btn.pack_forget()
    channel_name = connect(ip, nick)
    global nickname
    nickname = nick
    Channel(channels, channel_name).pack(fill=X)

def crt_proc(chn, nick):
    crt_lbl1.pack_forget()
    crt_chn.pack_forget()
    crt_lbl2.pack_forget()
    crt_nickname.pack_forget()
    crt_btn.pack_forget()

def send(txt):
    Message(messages, nickname, txt).pack(fill=X, side=BOTTOM)


menu = Menu(root, tearoff=0)
chatmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Chat", menu=chatmenu)
chatmenu.add_command(label="Connect", command=con)
chatmenu.add_command(label="Create", command=crt)

root.config(menu=menu)

frame1 = Frame(root, bg="#59981A", borderwidth=1)
frame2 = Frame(root, bg="#3D550C")
frame3 = Frame(frame1, bg="#3D550C")
channels = Frame(frame1).inherit_bg()
messages = Frame(frame2).inherit_bg()
enter_fr = Frame(frame2).inherit_bg()

#region create
crt_lbl1 =  Label(frame2, text="Enter channel name:", font=("Helvetica", 16)).inherit_bg()
crt_chn = Entry(frame2)
crt_lbl2 = Label(frame2, text="Enter nickname:", font=("Helvetica", 16)).inherit_bg()
crt_nickname = Entry(frame2)
crt_btn = Button(frame2, command=lambda: crt_proc(crt_chn.get(), crt_nickname.get()), text="Create", font=("Helvetica", 14))
#endregion

#region connect
con_lbl1 =  Label(frame2, text="Enter IP:", font=("Helvetica", 16)).inherit_bg()
con_ip = Entry(frame2)
con_lbl2 = Label(frame2, text="Enter nickname:", font=("Helvetica", 16)).inherit_bg()
con_nickname = Entry(frame2)
con_btn = Button(frame2, command=lambda: con_proc(con_ip.get(), con_nickname.get()), text="Connect", font=("Helvetica", 14))
#endregion

#chnl = Channel(channels, "Hello")
#message = Message(messages, "TAFH", "Hellow")
lbl = Label(frame3, text="Channels", font=("Helvetica", 32), bg="#3D550C", fg="#ECF87F")
entry = Entry(enter_fr, font=("Helvetica", 20), width=40)
btn = Button(enter_fr, text="Send", width=20, bg="#4c9a15", activebackground="#60a231", borderwidth=0, command=lambda: send(entry.get()))

frame1.pack(side=LEFT, fill=Y)
frame2.pack(side=LEFT, fill=BOTH, expand=1)
frame3.pack(side=TOP, fill=X)
channels.pack(fill=X)
enter_fr.pack(fill=X, side=BOTTOM)
messages.pack(fill=X, side=BOTTOM)

entry.pack(side=LEFT)
btn.pack(fill=Y, side=LEFT)
lbl.pack(padx=20, pady=20)
#chnl.pack(fill=X)
#message.pack(fill=X, side=BOTTOM)

root.mainloop()
