from tkinter import *

root = Tk(className = "button_click_label")
root.geometry("200x50")

message = StringVar()
message.set('hi')

l1 = Label(root, textvariable = message  ,fg = 'red', width = 20)


def press():
    message.set("Text Changed")

b1 = Button(root, text = "CLICK", command = press , fg = 'blue').pack(side= 'left')

b2 = Button(root, text = "QUIT", fg = 'blue', command = root.destroy).pack(side= 'left')
l1.pack()
root.mainloop()