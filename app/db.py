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

def create_where(select_query, keys):
    arg_query = " AND ".join(["{}=?".format(key) for key in keys])
    return "WHERE {}".format(arg_query)

def create_order(asc_list, desc_list):
    desc_list = ["{} DESC".format(desc) for desc in desc_list]
    desc_query = ",".join(desc_list)
    asc_query = ",".join(asc_list)
    query = [ q for q in [asc_query, desc_query] if q]
    return "ORDER BY {}".format(",".join(query))

def create_insert(table, keys):
    columns = ", ".join(keys)
    values =  ", ".join([":{}".format(key) for key in keys])
    return "INSERT INTO {} ({}) VALUES ({})".format(table, columns, values)

def create_update(table, keys):
    columns = ", ".join(keys)
    values =  ", ".join(["{}=:{}".format(key, key) for key in keys])
    return "UPDATE {} SET {} WHERE id=:id".format(table, values)

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def modify_db(query, args=()):
    con = get_db()
    try:
        with con:
            cur =con.cursor()
            cur.execute('pragma foreign_keys=ON')
            cur.execute(query, args)
            con.commit()
            cur.lastrowid
            return cur.lastrowid
    except sqlite3.IntegrityError as e:
        print query, args
        return False


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
