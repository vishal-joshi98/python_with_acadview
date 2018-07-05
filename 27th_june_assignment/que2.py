dic = {}
def printtext():
    global e

    string = e.get()
    print(string)

from tkinter import *
root = Tk()

root.title('ITEM')
Message(root, text= "ENTER KEY VALUE").pack()

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='SUBMIT',command=printtext)
b.pack(side='bottom')
print(dic)
root.mainloop()