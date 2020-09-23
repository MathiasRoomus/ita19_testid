import sqlite3
import csv

ühendus = sqlite3.connect('andmebaas.db')
maker = ühendus.cursor()


#maker.execute("CREATE TABLE laulud (artist text, album text, aasta text, laul text)")

tabel = []
with open("albumid.txt", encoding="utf-8") as fail:
    fail_lugeja = csv.reader(fail, delimiter="\t")
    for row in fail_lugeja:
        tabel.append(row)
        maker.execute("INSERT INTO laulud VALUES ('{0}','{1}','{2}','{3}')".format(row[0], row[1], row[2], row[3]))


#INSERT INTO õppijad VALUES ('Indrek','Kivi')
#"INSERT INTO laulud VALUES ('" + row[0] + "','" +
#asi = "INSERT INTO laulud VALUES ('{}','{}','{}','{}')".format(row[0],row[1],row[2],row[3])
#print(asi)





ühendus.commit()

ühendus.close()