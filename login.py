import sqlite3
from math import *
from tkinter import *
from datetime import datetime
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageDraw

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("User Login")
        self.root.geometry("1280x700+0+0")
        self.root.config(bg="#021e2f")

        # Background color
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        # Frames
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2")
        title.place(x=250, y=50)

        # Email
        email = Label(login_frame, text="Email Address", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        email.place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        # Password
        pass_ = Label(login_frame, text="Password", font=("times new roman", 18, "bold"), bg="white", fg="gray")
        pass_.place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        # Buttons
        btn_reg = Button(login_frame, text="Register New Account?", font=("times new roman", 14), bg="white", bd=0,
                         fg="#B00857", cursor="hand2", command=self.register)
        btn_reg.place(x=250, y=320)

        btn_login = Button(login_frame, text="Sign In", font=("times new roman", 20, "bold"), fg="white", bd=0,
                           bg="#B00857", cursor="hand2", command=self.login)
        btn_login.place(x=300, y=380, width=180, height=40)

        btn_forget = Button(login_frame, text="Forget Password?", font=("times new roman", 12), bg="white",bd=0, fg="#B00857", cursor="hand2", command=self.forgot_password)
        btn_forget.place(x=330, y=425)

        # Clock
        self.lbl = Label(self.root, text="\nWebCode Clock", font=("Book Antiqua", 25, "bold"), compound=BOTTOM,
                         bg="#081923", fg="white", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)

        # Start clock
        self.clock_img = None
        self.working()

    # Draw clock in memory (no disk saving)
    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)

        # Clock background
        bg = Image.open("images/c.png").resize((300, 300), Image.Resampling.LANCZOS)
        clock.paste(bg, (50, 50))

        origin = 200, 200
        # Hour hand
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="#DF005E", width=4)
        # Minute hand
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill="white", width=3)
        # Second hand
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill="yellow", width=2)
        # Center circle
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        return ImageTk.PhotoImage(clock)

    def working(self):
        now = datetime.now()
        h, m, s = now.hour, now.minute, now.second
        hr_angle = (h % 12 + m / 60) * 30        # Convert hour to degrees
        min_angle = (m + s / 60) * 6             # Convert minute to degrees
        sec_angle = s * 6                         # Convert second to degrees

        self.clock_img = self.clock_image(hr_angle, min_angle, sec_angle)
        self.lbl.config(image=self.clock_img)
        self.lbl.after(200, self.working)

    # Login validation
    def login(self):
        email = self.txt_email.get()
        password = self.txt_pass_.get()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required!", parent=self.root)
            return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            row = cur.fetchone()
            con.close()

            if row == None:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
            else:
                messagebox.showinfo("Success", f"Welcome {row[1]}!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def register(self):
        self.root.destroy()
        import register

    def forgot_password(self):
        email = self.txt_email.get()
        if not email:
            messagebox.showerror("Error", "Please enter your email to reset password.", parent=self.root)
            return

        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE email=?", (email,))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "This email is not registered.", parent=self.root)
                conn.close()
            else:
                conn.close()
                # Open reset password window
                self.root2 = Toplevel(self.root)
                self.root2.title("Forgot Password")
                self.root2.geometry("400x400+600+200")
                self.root2.config(bg="#1a1a2e")

                Label(self.root2, text="Reset Password", font=("times new roman", 22, "bold"), bg="#1a1a2e", fg="#e94560").pack(pady=10)

                Label(self.root2, text="Security Question:", font=("times new roman", 16, "bold"), bg="#1a1a2e", fg="white").pack(pady=5)
                self.security_q_combo = ttk.Combobox(self.root2, font=("times new roman", 14), state="readonly")
                self.security_q_combo["values"] = ("Select", "Your Birth Place", "Your Best Friend Name", "Your Pet Name")
                self.security_q_combo.current(0)
                self.security_q_combo.pack(pady=5, padx=20, fill=X)

                Label(self.root2, text="Answer:", font=("times new roman", 16, "bold"), bg="#1a1a2e", fg="white").pack(pady=5)
                self.security_a_entry = Entry(self.root2, font=("times new roman", 14))
                self.security_a_entry.pack(pady=5, padx=20, fill=X)

                Label(self.root2, text="New Password:", font=("times new roman", 16, "bold"), bg="#1a1a2e", fg="white").pack(pady=5)
                self.new_password_entry = Entry(self.root2, font=("times new roman", 14), show="*")
                self.new_password_entry.pack(pady=5, padx=20, fill=X)

                Button(self.root2, text="Reset Password", font=("times new roman", 16, "bold"),
                    fg="white", bg="green", cursor="hand2", command=self.reset_password).pack(pady=20)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def reset_password(self):
        email = self.txt_email.get()
        question = self.security_q_combo.get()
        answer = self.security_a_entry.get()
        new_password = self.new_password_entry.get()

        if question == "Select" or not answer or not new_password:
            messagebox.showerror("Error", "All fields are required!", parent=self.root2)
            return

        try:
            conn = sqlite3.connect("users.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE email=? AND question=? AND answer=?", (email, question, answer))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Security question/answer is incorrect!", parent=self.root2)
            else:
                cur.execute("UPDATE users SET password=? WHERE email=?", (new_password, email))
                conn.commit()
                messagebox.showinfo("Success", "Password has been reset successfully!", parent=self.root2)
                self.root2.destroy()
            conn.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root2)


root = Tk()
obj = Login(root)
root.mainloop()