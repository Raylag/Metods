import cgi
import sqlite3
from lxml import etree

print("Content-Type: text/html")
print()

con = sqlite3.connect('DataArc.db')
cursor = con.cursor()

form = cgi.FieldStorage()
if "xml_file" not in form:
    print("<h2>The file has not been uploaded!</h2>")
else:
    xml_file = form["xml_file"].file

    try:
        tree = etree.parse(xml_file)
        root = tree.getroot()

        cursor.execute("DELETE FROM Work")
        cursor.execute("DELETE FROM Cont")
        cursor.execute("DELETE FROM Architects")

        architects = root.findall('Architects/Architect')
        for architect in architects:
            name = architect.text
            cursor.execute("INSERT INTO Architects (name) VALUES (?)", (name,))

        cont = root.findall('Cont/Contik')
        for cont_one in cont:
            Style = cont_one.text
            ArchitectId = cont_one.get('ArchitectId')
            cursor.execute("INSERT INTO Cont (Style, ArchitectId) VALUES (?, ?)", (Style, ArchitectId))

        work = root.findall('Work/Working')
        for working in work:
            price = working.text
            cont_id = working.get('Cont_id')
            cursor.execute("INSERT INTO Work (Price, cont_id) VALUES (?, ?)", (price, cont_id))

        con.commit()
        print("<h2>The database has been successfully updated!</h2>")
    except Exception as e:
        print(f"<h2>Error loading the database: {e}</h2>")

con.close()