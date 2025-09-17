import sqlite3
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(
            self.root,
            text="View Student Results",
            font=("goudy old style", 20, "bold"),
            bg="orange",
            fg="#262626"
        ).place(x=10, y=15, width=1180, height=50)

if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()