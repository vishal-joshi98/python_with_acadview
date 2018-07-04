from tkinter import *
from tkinter import messagebox
class C_text:
    def __init__(self, Master):
        """
        THIS WILL CREATE TWO BUTTON EXIT AND CLICK FOR MAGIC
        WHEN YOU CLICK ON BUTTON CLICK FOR MAGIC IT WILL POPUP NEW MEASSAGE

        :param Master: PARENT WIDGET
        :return:
        """
        frame = Frame(Master)
        frame.pack()
        self.button = Button(frame, text = 'Exit', width=20,  fg = 'blue', command = Master.quit)
        self.button.pack(side = 'left')
        self.hi_there = Button(frame, text = 'Click for Magic', fg= 'blue' ,width=20, command = self.say_hi)
        self.hi_there.pack(side = 'left')
    def say_hi(self):
        messagebox.showinfo("Welcom Ji", "Welcome to New Era")    # SHOWING NEW MESSAGE WHEN CLICK O BUTTON

root = Tk()
root.title('Text on click')

txt = Label(root, text='Hello World', width=20, height=1)  # write the text on tkinter interface
txt.pack()
app = C_text(root)
root.mainloop()
