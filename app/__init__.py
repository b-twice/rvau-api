#!flask/bin/python
from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


# auth
CLIENT_ID="TPZrTRxzqYySVXNwNsokXsFL25cTD1ML" 
CLIENT_SECRET="uf6A8G-mcB2MyMUhKtPa9k1FeKlDs9BkgTlds2b5NICeS5iFN4rAaluNpsJz3V5F"
DOMAIN="bgeo.auth0.com" 
CALLBACK_URL="http://localhost:3000/callback"

# Add Access Control Header
CORS(app, orgins=["http://localhost:8000"])
import db, api

# Can't get this to configure to CLI
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'
