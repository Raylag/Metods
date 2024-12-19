import sqlite3
from lxml import etree

con = sqlite3.connect('DataArc.db')
cursor = con.cursor()

root = etree.Element('ArchitectureBase')

cursor.execute("SELECT * FROM Architects")
architects = cursor.fetchall()
architects_element = etree.SubElement(root, 'Architects')

for architect in architects:
    architects_element = etree.SubElement(architects_element, 'Architect', id=str(architect[0]))
    architects_element.text = architect[1]

cursor.execute("SELECT * FROM Cont")
cont_one = cursor.fetchall()
cont_more_element = etree.SubElement(root, 'Cont')

for cont in cont_one:
    cont_one_element = etree.SubElement(cont_more_element, 'Contik', id=str(cont[0]), ArchitectId=str(cont[2]))
    cont_one_element.text = cont[1]

cursor.execute("SELECT * FROM Work")
price = cursor.fetchall()
price_pop = etree.SubElement(root, 'Work')

for pricek in price:
    track_element = etree.SubElement(price_pop, 'Pricek', id=str(pricek[0]), album_id=str(pricek[2]))
    track_element.text = pricek[1]

with open('Architecture_database.xml', 'wb') as xml_file:
    xml_file.write(etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8'))

con.close()