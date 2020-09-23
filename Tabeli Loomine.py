import sqlite3
import csv

ühendus = sqlite3.connect('andmebaas.db')
maker = ühendus.cursor()


maker.execute("CREAT TABLE laulud (artist text, album text, aasta text, laul text")

tabel = []
with open("albumid.txt", encoding="utf-8") as fail:
    fail_lugeja = csv.reader(fail, delimiter="\t")
    for row in fail_lugeja:
        tabel.append(row)

artist = []
album = []
laul = []
aasta = []






ühendus.commit()

ühendus.close()