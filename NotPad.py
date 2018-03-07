from Tkinter import *
import tkFileDialog
import tkMessageBox
root = Tk(className=" !Pad ")
root.attributes('-alpha', 0.8)
root.config(bg='black')
text = Text(root)
#text.attributes('-alpha', 0.3)
text.config(fg='green', bg='black', highlightthickness=0, insertbackground='white', tabs='1c')
#print('\n + %s' % dir(text))
#text["geometry"] = "1920x1080"
text.insert(END, "<!--!Pad v1.0.0 beta - A project by Bhavdeep Singh--> \n\n")
text.pack(side=LEFT, fill=BOTH, expand = YES)

menu = Menu(root)

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()


root.config(menu=menu)
FileMenu=Menu(menu)
menu.add_cascade(label="File", menu=FileMenu)
FileMenu.add_command(label="New", command=saveas)
FileMenu.add_command(label="Save", command=saveas)
FileMenu.add_command(label="Open", command=saveas)

def fontHelvetica():
    global text
    text.config(font = "Helvetica")
def fontCourier():
    global text
    text.config(font = "Courier")

FontMenu=Menu(menu)
menu.add_cascade(label="Font", menu=FontMenu)
FontMenu.add_command(label="Helvetica", command=fontHelvetica)
FontMenu.add_command(label="Courier", command=fontCourier)

def aboutFunc():
    tkMessageBox.showinfo('Title', 'You\'ll be fine! You\'re fine!')

AboutMenu=Menu(menu)
menu.add_cascade(label="About", menu=AboutMenu)
AboutMenu.add_command(label="About", command=aboutFunc)
root.mainloop()