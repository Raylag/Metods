import sqlite3
from lxml import etree

print("Content-Type: application/xml")
print("Content-Disposition: attachment; filename=ArchitectureBase.xml")
print()

conn = sqlite3.connect('DataArc.db')
cursor = conn.cursor()

root = etree.Element('ArchitectureBase')

cursor.execute("SELECT * FROM Architects")
architects = cursor.fetchall()
architects_element = etree.SubElement(root, 'Architects')

for architect in architects:
    architect_element = etree.SubElement(architects_element, 'Architect')
    architect_element.text = architect[1]

cursor.execute("SELECT * FROM Cont")
cont = cursor.fetchall()
cont_one_element = etree.SubElement(root, 'Cont')

for cont_no_one in cont:
    cont_no_one_element = etree.SubElement(cont_one_element, 'Contik', ArchitectId=str(cont_no_one[2]))
    cont_no_one_element.text = cont_no_one[1]

cursor.execute("SELECT * FROM Work")
work = cursor.fetchall()
work_pop = etree.SubElement(root, 'Work')

for working in work:
    working_pop = etree.SubElement(work_pop, 'Work', album_id=str(working[2]))
    working_pop.text = working[1]

print(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8').decode('UTF-8'))

conn.close()