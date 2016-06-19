import sqlite3

db = r"C:\Users\bgeo-win\Documents\git\rvau-api\app.db"
connection = sqlite3.connect(db)


data = {"league_type": "Winter", "league_year": "2016"}

def create_insert(table, keys):
	columns = ", ".join(keys)
	values =  ", ".join([":{}".format(key) for key in keys])
	return "INSERT INTO {} ({}) VALUES ({})".format(table, columns, values)

insert = create_insert("League", data.keys())

# with connection:
# 	print insert
# 	cursor = connection.cursor()
# 	cursor.execute("INSERT INTO League VALUES(2018, 'Winter')")

print insert
data
with connection:
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM LEAGUE")
	print cursor.fetchall()
