from tkinter import *
from result import Result
from course import Course
from student import Student
from PIL import Image, ImageTk


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg="white")

        # Icons
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # Title
        title = Label(
            self.root,
            text="Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=0, y=0, relwidth=1, height=50)

        # Menu
        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("Times new roman", 15),
            bg="white"
        )
        M_Frame.place(x=10, y=60, width=1260, height=80)

        # Buttons
        btn_course = Button(
            M_Frame,
            text="Course",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_course
        ).place(x=20, y=5, width=195, height=40)

        btn_student = Button(
            M_Frame,
            text="Student",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_student
        ).place(x=225, y=5, width=195, height=40)

        btn_result = Button(
            M_Frame,
            text="Result",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2",
            command=self.add_result
        ).place(x=430, y=5, width=195, height=40)

        btn_view = Button(
            M_Frame,
            text="View Student Results",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2"
        ).place(x=635, y=5, width=195, height=40)

        btn_logout = Button(
            M_Frame,
            text="Logout",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2"
        ).place(x=840, y=5, width=195, height=40)

        btn_exit = Button(
            M_Frame,
            text="Exit",
            font=("goudy old style", 15, "bold"),
            bg="#0b5377",
            fg="white",
            cursor="hand2"
        ).place(x=1045, y=5, width=195, height=40)

        # Content
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((850, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=400, y=180, width=850, height=350)

        # Update Details
        self.lbl_course = Label(
            self.root,
            text="Total Courses\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#e43b06",
            fg="white"
        )
        self.lbl_course.place(x=400, y=530, width=275, height=100)

        self.lbl_student = Label(
            self.root,
            text="Total Students\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#0676ad",
            fg="white"
        )
        self.lbl_student.place(x=685, y=530, width=275, height=100)

        self.lbl_result = Label(
            self.root,
            text="Total Results\n[ 0 ]",
            font=("goudy old style", 20),
            bd=10,
            relief=RIDGE,
            bg="#038074",
            fg="white"
        )
        self.lbl_result.place(x=970, y=530, width=275, height=100)

        # Footer
        footer = Label(
            self.root,
            text="SRMS-Student Result Management System\nContact Us For Any Technical Issue: sdebidutta2020@gmail.com",
            font=("goudy old style", 12),
            bg="#262626",
            fg="white"
        ).pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Course(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()