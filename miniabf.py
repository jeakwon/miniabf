"""
MiniAbf
Simple GUI ABF1 converter for MiniAnalysis users 
created by Jea Kwon 2020-02-07
Thanks to swharden, pyabf lib author.
"""
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import pyabf 

root = tk.Tk()
root.title("Convert To ABF1")
root.geometry('900x400')



def main():
    T = Text(root, height=20, width=50)
    T.pack(expand=True, fill='both')

    def convert():
        files = tk.filedialog.askopenfilenames(
            parent=root, 
            title='Select .abf Files', 
            filetypes = (("abf files","*.abf"),("all files","*.*"))
        )

        for i, file in enumerate(files, start=1):
            abf = pyabf.ABF(file)
            name, ext = os.path.splitext(file)
            newfile = name+"_abf1"+ext
            abf.saveABF1(newfile, abf.dataRate)
            T.insert(END, f"[{i}/{len(files)}]Converted... {newfile}\n")
            root.update()
        T.insert(END, f"Completed! {newfile}\n")

    B = Button(root, text="Convert to ABF1", command=convert, height=3, width=20)
    B.pack(side=LEFT)
    L = Label(root, text="2020. 02. 07 created by Jea Kwon  \n https://github.com/jeakwon/miniabf  ", height=3, width=30, anchor=W)
    L.pack(side=RIGHT)

if __name__ == "__main__":
    main()
    root.mainloop()
