from tkinter import *
root = Tk()
root.geometry("200x100")

def retrive_input():    #simple function to store to variable on button press
    inputValue = textBox.get("1.0","end-1c")  #our variable
    #1.0 = start from first character in the texxt widget
    #end-1 = delete the last character that text create every time
    print(inputValue)#just print

textBox = Text(root, height = 2, width = 10)  #text widget
textBox.pack()
buttonCommit = Button(root, height=1, width = 10 , text = "Commit", command = lambda: retrive_input())
# create  a button
# command = lambda: retrive_inputs() = do this command after button is clicked
# basically lambda  states "dont do stuff untill button  is pushed"

buttonCommit.pack()
mainloop()