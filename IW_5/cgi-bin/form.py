import cgi
import cgitb; cgitb.enable()
import sqlite3
print("Content-type: text/html")
print()


form = cgi.FieldStorage()
# name = form.getfirst("Name", "123")
# style = form.getfirst("Style", "123")
# price = form.getfirst("Price", "123")
# arg1=[
#     name,
#     style,
#     price
# ]
name = form.getvalue('name')
style = form.getvalue('style')
price = form.getvalue('price')
con = sqlite3.connect('DataArc.db')
cur = con.cursor()
def get_or_insert_architect(name):
    cur.execute("SELECT id FROM Architects WHERE name = ?", (name,))
    architect = cur.fetchone()
    if architect:
        return architect[0]
    else:
        cur.execute("INSERT INTO Architects (name) VALUES (?)", (name,))
        con.commit()
        return cur.lastrowid

def get_or_insert_contik(style, architectId):
    cur.execute("SELECT id FROM Cont WHERE style = ? AND architectId = ?", (style, architectId))
    contik = cur.fetchone()
    if contik:
        return contik[0]
    else:
        cur.execute("INSERT INTO Cont (style, architectId) VALUES (?, ?)", (style, architectId))
        con.commit()
        return cur.lastrowid

architectId = get_or_insert_architect(name)

Cont_id = get_or_insert_contik(style, architectId)

if price and Cont_id:
    cur.execute("INSERT INTO Work (Price, Cont_id) VALUES (?, ?)", (price, Cont_id))
    con.commit()

# def get_or_insert_working(price):
#     cur.execute("SELECT id FROM Cont WHERE price = ?", (price,))
#     working = cur.fetchone()
#     if working:
#         return working[0]
#     else:
#         cur.execute("INSERT INTO Cont (price) VALUES (?)", (price,))
#         con.commit()
#         return cur.lastrowid

con.close()

# sql1='''INSERT INTO Cont (Style,Materials,ArchitectId) VALUES(?,?,?)'''
# cur.execute(sql1,arg1)
# con.commit()

print("<html><body>")
print("<h1>Has been added!</h1>")
print('<a href="/index.html">Back</a>')
print("</body></html>")

