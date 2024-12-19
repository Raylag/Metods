import sqlite3
from lxml import etree


conn = sqlite3.connect('DataArc.db')
cursor = conn.cursor()

tree = etree.parse('Architecture_database.xml')
root = tree.getroot()

architects = root.findall('Architects/Architect')
for architect in architects:
    name = architect.text
    cursor.execute("INSERT INTO Architects (name) VALUES (?)", (name,))

cont_one = root.findall('Cont/Contik')
for cont in cont_one:
    Style = cont.text
    ArchitectId = cont.get('ArchitectId')
    cursor.execute("INSERT INTO Cont (Style, ArchitectId) VALUES (?, ?)", (Style,  ArchitectId))

work = root.findall('Work/Working')
for working in work:
    price = working.text
    cont_id = working.get('cont_id')
    cursor.execute("INSERT INTO Work (price, cont_id) VALUES (?, ?)", (price, cont_id))

conn.commit()
conn.close()