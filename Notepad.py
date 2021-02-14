from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def NewFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)
def OpenFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes=[("All Files","*.*"),
                                                                 ("Text Documents","*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()


def NewWindow():
    pass
def PageSetup():
    pass
def Print():
    pass

def Save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes=[("All Files","*.*"),
                                                                 ("Text Documents","*.txt")])

        if file == "":
            file = None
        else:
            f = open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            print("File Saved")
    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def SaveAs():
    global file
    if file != None or file == None:
        file = asksaveasfilename(initialfile=file, defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                      "*.txt")])

        if file == "":
            file = None
        else:
            f = open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")
            print("File Saved")


    else:
        f = open(file, 'w')
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

#Edit menu functions
def Undo():
    TextArea.event_generate("<<Undo>>")
def cut():
    TextArea.event_generate("<<Copy>>")
def Copy():
    TextArea.event_generate("<<Copy>>")
def Paste():
    TextArea.event_generate("<<Paste>>")
def Delete():
    TextArea.event_generate("<<Delete>>")

#Help menu functions
def ViewHelp():
    pass
def SendFeedback():
    pass
def About():
    showinfo("Notepad", "Notepad by Abhishek Pandey")


if __name__ == '__main__':
    root = Tk()
    root.title('Untitled - Notepad')
    root.geometry('655x655')
    root.wm_iconbitmap('n.ico')

    #Add text area
    TextArea = Text(root,font = 'Lucida 13')
    file = None
    TextArea.pack(expand = True,fill = BOTH)

    #menu bar
    mymenu = Menu(root)
    #File menu
    m1 = Menu(mymenu, tearoff=0)
    m1.add_command(label="New", command=NewFile)
    m1.add_command(label="Open", command=OpenFile)
    m1.add_command(label="New Window", command=NewWindow)
    m1.add_separator()
    m1.add_command(label="Page Setup", command=PageSetup)
    m1.add_command(label="Print", command=Print)
    m1.add_separator()
    m1.add_command(label="Save", command=Save)
    m1.add_command(label="Save As", command=SaveAs)
    m1.add_separator()
    m1.add_command(label="Exit", command=quitApp)
    root.config(menu=mymenu)
    mymenu.add_cascade(label="File", menu=m1)

    #Edit menu
    m2 = Menu(mymenu, tearoff=0)
    m2.add_command(label="Undo", command=Undo)
    m2.add_separator()
    m2.add_command(label="Cut", command=cut)
    m2.add_command(label="Copy", command=Copy)
    m2.add_command(label="Paste", command=Paste)
    m2.add_separator()
    m2.add_command(label="Delete", command=Delete)
    root.config(menu=mymenu)
    mymenu.add_cascade(label="Edit", menu=m2)

    #Help menu
    m5 = Menu(mymenu, tearoff=0)
    m5.add_command(label="View Help", command=ViewHelp)
    m5.add_command(label="Send Feedback", command=SendFeedback)
    m5.add_separator()
    m5.add_command(label="About Notepad", command=About)
    root.config(menu=mymenu)
    mymenu.add_cascade(label="Help", menu=m5)

    # Add scroll bar
    scrollbar = Scrollbar(TextArea)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollbar.set)

    root.mainloop()