import os
import sqlite3
from math import *
from tkinter import *
from datetime import *
from course import Course
from result import Result
from report import Report
from student import Student
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


SESSION_FILE = "session.txt"

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg="white")

        # Check session
        self.user_email = self.check_session()
        if not self.user_email:
            messagebox.showwarning("Unauthorized", "You must login first!")
            self.root.destroy()
            os.system("python login.py")
            return

        # Get user's first name from DB
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT fname FROM users WHERE email=?", (self.user_email,))
            row = cur.fetchone()
            con.close()
            self.user_name = row[0] if row else "User"
        except:
            self.user_name = "User"

        # Icons
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        # Title
        title = Label(
            self.root,
            text=f"Welcome, {self.user_name} - Student Result Management System",
            padx=10,
            compound=LEFT,
            image=self.logo_dash,
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        ).place(x=0, y=0, relwidth=1, height=50)

        # Menu Frame
        M_Frame = LabelFrame(self.root, text="Menus", font=("Times new roman", 15), bg="white")
        M_Frame.place(x=10, y=60, width=1260, height=80)

        # Menu Buttons
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=5, width=195, height=40)

        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"),
                             bg="#0b5377", fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=225, y=5, width=195, height=40)

        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=430, y=5, width=195, height=40)

        btn_view = Button(M_Frame, text="View Student Results", font=("goudy old style", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2", command=self.view_report)
        btn_view.place(x=635, y=5, width=195, height=40)

        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=840, y=5, width=195, height=40)

        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2", command=self.exit_)
        btn_exit.place(x=1045, y=5, width=195, height=40)

        # Content
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((850, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=850, height=350)

        # Stats
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400, y=530, width=275, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20),
                                 bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=685, y=530, width=275, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20),
                                bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=970, y=530, width=275, height=100)

        # Clock
        self.lbl = Label(self.root, text="\nWebCode Clock", font=("Book Antiqua", 25, "bold"),
                         compound=BOTTOM, bg="#081923", fg="white", bd=0)
        self.lbl.place(x=20, y=180, height=450, width=350)

        # Start clock
        self.clock_img = None
        self.working()

        # Footer
        footer = Label(self.root,
                       text="SRMS-Student Result Management System\nContact: sdebidutta2020@gmail.com",
                       font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        # Update details
        self.update_details()

    def check_session(self):
        if os.path.exists(SESSION_FILE):
            with open(SESSION_FILE, "r") as f:
                email = f.read().strip()
                return email
        return None

    def update_details(self):
        con = sqlite3.connect("rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{len(cr)}]")

            cur.execute("SELECT * FROM student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{len(cr)}]")

            cur.execute("SELECT * FROM result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{len(cr)}]")

            self.lbl_course.after(200, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error!", f"Error Due To: {str(ex)}.", parent=self.root)

    # Clock
    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png").resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg, (50, 50))
        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=4)
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        return ImageTk.PhotoImage(clock)

    def working(self):
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second
        hr_angle = (h % 12 + m / 60) * 30
        min_angle = (m + s / 60) * 6
        sec_angle = s * 6
        self.clock_img = self.clock_image(hr_angle, min_angle, sec_angle)
        self.lbl.config(image=self.clock_img)
        self.lbl.after(200, self.working)

    # Menu actions
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Course(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Student(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win)

    def view_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Report(self.new_win)

    def logout(self):
        if messagebox.askyesno("Confirm!", "Do you really want to logout?", parent=self.root):
            if os.path.exists(SESSION_FILE):
                os.remove(SESSION_FILE)
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        if messagebox.askyesno("Confirm!", "Do you really want to exit?", parent=self.root):
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()