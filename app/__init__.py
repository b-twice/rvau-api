#!flask/bin/python
from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


# Add Access Control Header
CORS(app, orgins=["http://localhost:8000"])
import db, api

# Can't get this to configure to CLI
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'
