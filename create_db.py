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
    
    cur.execute('''CREATE TABLE IF NOT EXISTS result (
                    rid INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll TEXT,
                    name TEXT,
                    course TEXT,
                    marks_ob TEXT,
                    full_marks TEXT,
                    per TEXT
                )''') 
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT,
        lname TEXT,
        contact TEXT,
        email TEXT UNIQUE,
        question TEXT,
        answer TEXT,
        password TEXT
    )""")
    
    con.commit()
    con.close()
create_db()