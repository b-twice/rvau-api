#!flask/bin/python
from app import app
from flask import Flask, g
import sqlite3


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

DATABASE = app.config["DATABASE_URI"]
def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	db.row_factory = make_dicts
	return db

def create_where(query, keys):
	arg_query = " AND ".join(["{}=?".format(key) for key in keys])
	return "{} WHERE {}".format(query, arg_query)

def create_insert(table, keys):
	columns = ", ".join(keys)
	values =  ", ".join([":{}".format(key) for key in keys])
	return "INSERT INTO {} ({}) VALUES ({})".format(table, columns, values)

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

def insert_db(query, args=()):
	con = get_db()
	try:
	    with con:
	        con.execute(query, args)
    		con.commit()
    		return True, args
	except sqlite3.IntegrityError:
	    return (False, {"Post": "Record already exists"})


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, "_database", None)
	if db is not None:
		db.close()