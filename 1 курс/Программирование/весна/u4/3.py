import sqlite3
connection = sqlite3.connect('C:/Users/seray/Desktop/учёба/прога/весна/u4/music.db')
cursor = connection.cursor()

#cursor.execute('''
#               CREATE TABLE IF NOT EXISTS tMusician (
#               id INTEGER PRIMARY KEY, 
#               псевдоним TEXT NOT NULL,
#               возраст INTEGER,
#               пол TEXT NOT NULL)''')
#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS tSongs (
#               id INTEGER PRIMARY KEY AUTOINCREMENT,
#               название TEXT NOT NULL,
#               описание TEXT,
#               id_музыканта INTEGER,
#               FOREIGN KEY (id_музыканта) REFERENCES tMusician(id) ON DELETE CASCADE);''')
#cursor.execute('''
#    CREATE TABLE IF NOT EXISTS tComments (
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    текст_комментария TEXT NOT NULL,
#    id_песни INTEGER,
#    id_музыканта INTEGER,
#    FOREIGN KEY (id_песни) REFERENCES tSongs(id) ON DELETE CASCADE,
#    FOREIGN KEY (id_музыканта) REFERENCES tMusician(id) ON DELETE CASCADE
#);
#''')

cursor.execute("SELECT * FROM tMusician")
for i in range(5):
    print(cursor.fetchone())
print()

cursor.execute("SELECT * FROM tSongs")
print(cursor.fetchmany(3), '\n')


cursor.execute("SELECT * FROM tComments")
print(cursor.fetchall())

connection.commit()
connection.close()