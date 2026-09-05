import sqlite3
'''
try:
    connection = sqlite3.connect('sqlitePy.db')
    cursor = connection.cursor()
    print("База данных создана успешно и подключена к SQLite")
    select_query = "select sqlite_version();"
    cursor.execute(select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")
'''
connection = sqlite3.connect('C:/Users/seray/Desktop/учёба/прога/весна/u4/city.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS city (
               номер_п_п INTEGER PRIMARY KEY, 
               название_города TEXT NOT NULL)''')
cities = ['Москва', 'Санкт-Петербург', 'Тюмень', 'Красноярск', 'Владивосток']

for city in cities:
    cursor.execute('INSERT INTO city (название_города) VALUES (?)', (city,))

cursor.execute("SELECT * FROM city")
print(cursor.fetchone())

#cursor.execute("SELECT * FROM city")
print(cursor.fetchmany(3), '\n')


#cursor.execute("SELECT * FROM city")
print(cursor.fetchall())

connection.commit()
connection.close()