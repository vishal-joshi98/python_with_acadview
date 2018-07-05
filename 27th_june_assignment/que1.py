from tkinter import *
root = Tk()
root.geometry("20x50")
dic = {'vishal':9872139933, 'vivek':8847235763, 'vikram':8107683514,'vinod':9772589595,'vishkha':9872139933, 'vipul':8847235763, 'VIKASH':8107683514,'Ram':9772589595}
root.title("Scrollbar")
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill = Y)
mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in dic.keys():
    mylist.insert(END, str(line))
mylist.pack(side=LEFT,fill = BOTH)
scrollbar.config(command = mylist.yview)
mainloop()