import sqlite3

ühendus = sqlite3.connect('andmebaas.db')
maker = ühendus.cursor()








ühendus.commit()

ühendus.close()