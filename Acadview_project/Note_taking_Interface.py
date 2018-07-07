from tkinter import *
import tkinter.font as tkfont
root = Tk()
root.geometry("630x500")
root.title("Note Taking App")
font1 = tkfont.Font(family='Helvetica', size=15, weight='bold')
font_search_text = tkfont.Font(family='Helvetica', size=15)
font_search_btn = tkfont.Font(family='Helvetica', size=10, weight='bold')
font_note = tkfont.Font(family='Helvetica', size=15)
add_button = Button(root, width=20, bg="red", fg="white", text="Add New Note>>", font=font1,
                         )
add_button.place(x=20, y=20)
list_all_btn = Button(root, width=20, bg="red", fg="white", text="List All Notes", font=font1,
                           )
list_all_btn.place(x=290, y=20)
search_label = Label(root, text="Search Notes", font=font1)
search_label.place(x=20, y=90)
var = StringVar()
search_box = Entry(root, width=40, textvariable=var, font=font_search_text)
search_box.place(x=20, y=130)
search_button = Button(root, bg="red", fg="white", text="Search", font=font_search_btn, width=13,
                            )
search_button.place(x=470, y=130)
note_label = Label(root, text="-- Notes --", font=font1)
note_label.place(x=205, y=170)

listbox = Listbox(root, selectmode=SINGLE, width=630, font=font_note, height=12)
scroll = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
listbox['yscroll'] = scroll.set
scroll.pack(side="right", fill="y")
scroll.place(x=615, y=200, height=300)
mainloop()