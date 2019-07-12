from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file   # so that we can edit it
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)   #  (1.0, END) means starting from 1st line 0th character and delete upto end

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents", "*.txt")])
    if file=="":   
        file = None
    else:
        root.title(os.path.basename(file)  + "-Notepad")
        TextArea.delete(1.0, END)
        f= open(file, "r")
        TextArea.insert(1.0, f.read())   # means everything thats in file is dispalyed on TextArea
        f.close()
        
def saveFile():
    global file
    if file == None:   # it's the case when we save a new file which we called as     Save as
        file = asksaveasfilename(initialfile = "Untitled.txt",defaultextension=".txt", filetypes=[("All Files","*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            # save as new file
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File saved")

    else:  # then previous content is replaced by new
        f=open(file,"w")
        f.write(TextArea.get(1.0, END))
        f.close()
                               

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))    # handeled by tkinter

def copy():
    TextArea.event_generate(("<<Copy>>"))    # handeled by tkinter

def paste():
    TextArea.event_generate(("<<Paste>>"))    # handeled by tkinter

def about():
    showinfo("Notepad"," Notepad by Sanchit")


if __name__ == '__main__':
    # Basic tkinter setup
    root =Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad_icon.ico")
    root.geometry("644x700")

    # add textarea
    TextArea = Text(root, font="lucida 13")
    file = None  # this file points to currently open file which initially is none
    TextArea.pack(expand=True,fill=BOTH)
    # Menu bar
    MenuBar = Menu(root)

    #  FILE MENU STARTS
    FileMenu = Menu(MenuBar,tearoff=0)
    # Open a new file
    FileMenu.add_command(label = "New",command  = newFile)
    # open Existing file
    FileMenu.add_command(label = "Open",command = openFile)
    # Save current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label ="File", menu = FileMenu)
    #  FILE MENU ENDS


                                                    #  EDIT MENU STARTS
    EditMenu = Menu(MenuBar,tearoff=0)
    # Features of  CUT, COPY , PASTE
    EditMenu.add_command(label = "Cut",command  = cut)
    EditMenu.add_command(label = "Copy",command = copy)
    EditMenu.add_command(label = "Paste", command = paste)

    MenuBar.add_cascade(label ="Edit", menu = EditMenu)
                                                       #  EDIT MENU ENDS


    #                                            HELP MENU STARTS
    HelpMenu = Menu(MenuBar, tearoff = 0)
    HelpMenu.add_command(label = "About notepad",command =about)
    MenuBar.add_cascade(label ="Help", menu = HelpMenu)
    #                                            HELP MENU  ENDS

    root.config(menu = MenuBar)

                                             #      scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side = RIGHT, fill=Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)

    
    root.mainloop()






