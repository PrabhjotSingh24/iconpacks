"""File not completed as of now"""
from tkinter import *
from main import IconPack

root=Tk()
root.title("Icon Pack Files Generator")
root.geometry("500x500")
root.resizable(False, False)
text=Label(root, text="Icon Pack Files Generator", font=("Arial", 20))
text.place(anchor=N, relx=0.5, rely=0.1)
top_frame=Frame(root)
top_frame.place(anchor=S, relx=0.5, rely=0.5)
button=Button(top_frame, text="Generate", font=("Arial", 20))
button.grid(row=0, column=0)
button=Button(top_frame, text="Generate", font=("Arial", 20))
button.grid(padx=10,row=0, column=1)
root.mainloop()

#TODO add entry widgets to get the paths and ui for getting the name of an icon if wrong which destorys after the name is entered
