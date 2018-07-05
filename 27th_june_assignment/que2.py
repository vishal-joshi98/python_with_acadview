dic = {}


def item_insert():
    global key ,value
    k = key.get()
    v = value.get()

    dic[k]=v
    print(dic)

from tkinter import *

root = Tk()

root.title('ITEM')
Label(root, text="ENTER KEY AND VALUE").grid(row=3,column=1)
Label(root, text="key").grid(row=0)
Label(root , text="value").grid(row=1)
key = Entry(root)
value = Entry(root)
key.grid(row=0,column=1)
value.grid(row=1, column=1)


b = Button(root, text='SUBMIT', command=item_insert).grid(row=2,column=1)
root.mainloop()