import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI = 'app.db'
YOURAPPLICATION_SETTINGS=os.path.join(basedir, 'config.py')
DEBUG=True