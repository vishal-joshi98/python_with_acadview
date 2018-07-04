from tkinter import *
win = Tk()
win.title('Text')
txt = Label(win, text = 'Hello World')   # write the text on tkinter interface
txt.pack()
bt =Button(win, text = 'Exit', width=50, height=1,  command = win.destroy)  # create button
bt.pack()
win.mainloop()