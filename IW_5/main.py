import sqlite3

con = sqlite3.connect('DataArc.db')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Architects')
cur.execute('DROP TABLE IF EXISTS Cont')
cur.execute('DROP TABLE IF EXISTS Work')
cur.fetchall()
cur.execute('''CREATE TABLE Architects(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30),
            surname VARCHAR(30),
            WorkExperience   INTEGER,
            phone VARCHAR(30))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Cont(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Style VARCHAR(30),
            Materials VARCHAR(30),
            ArchitectId INTEGER,
            FOREIGN KEY (ArchitectId) REFERENCES Architects(id))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Work(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Price INTEGER,
            Days INTEGER,
            Cont_id Integer,
            FOREIGN KEY (Cont_id) REFERENCES Cont(id))''')

architects=[
    ("Alvaro","Siza","35","+19243641488"),
    ("Antonio","Predock","24","+99146181337"),
    ("Andre","Diakonov","3","+79283572648")
]
Cont=[
    ("Modern","Polypropylene", 2),
    ("Gotic","Stone",1),
    ("Loft","Brick",3)
]
work=[
    ("750000", "50", 2),
    ("530000", "46", 3),
    ("984000", "78", 1)
]

sqlE='''INSERT INTO Architects(name,surname,WorkExperience,phone) VALUES (?,?,?,?)'''
sqlA='''INSERT INTO Cont(style,materials,ArchitectId) VALUES (?,?,?)'''
sqlC='''INSERT INTO Work(Price,Days,Cont_id) VALUES (?,?,?)'''

cur.executemany(sqlE,architects)
cur.executemany(sqlA,Cont)
cur.executemany(sqlC,work)

con.commit()
con.close()
