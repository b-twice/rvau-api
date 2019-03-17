#!flask/bin/python
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object('config')
api = Api(app)


# CORS
# cors = CORS(app, origins=["http://localhost:8080", "http://rvau.bgeo.io"])
cors = CORS(app, origins=["https://rvau.brianbrown.dev"])

# auth
CLIENT_ID="TPZrTRxzqYySVXNwNsokXsFL25cTD1ML" 
CLIENT_SECRET="uf6A8G-mcB2MyMUhKtPa9k1FeKlDs9BkgTlds2b5NICeS5iFN4rAaluNpsJz3V5F"
DOMAIN="bgeo.auth0.com" 
CALLBACK_URL="http://localhost:3000/callback"

import db, api

# Can't get this to configure to CLI
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'
