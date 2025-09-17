import sqlite3

def create_db():
    con = sqlite3.connect('rms.db')
    cur = con.cursor()
    
    # Create tables
    cur.execute('''CREATE TABLE IF NOT EXISTS course (
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    duration TEXT NOT NULL,
                    charges TEXT NOT NULL,
                    description TEXT
                )''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS student (
                    roll INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    gender TEXT,
                    dob TEXT,
                    contact TEXT,
                    admission TEXT,
                    course TEXT,
                    state TEXT,
                    city TEXT,
                    pin TEXT,
                    address TEXT
                )''')
    
    # cur.execute('''CREATE TABLE IF NOT EXISTS result (
    #                 id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                 student_id INTEGER,
    #                 subject TEXT NOT NULL,
    #                 marks REAL NOT NULL,
    #                 FOREIGN KEY(student_id) REFERENCES student(id)
    #             )''')
    
    con.commit()
    con.close()
create_db()