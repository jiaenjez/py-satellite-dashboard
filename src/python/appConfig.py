import urllib
import os
from dotenv import load_dotenv
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


# db/memcache config setting
enableDB = False
enableMemcache = True

# flask config
app = Flask(__name__)
CORS(app)

# load secret from .env
load_dotenv()
dbUrl = os.getenv('DB_URL')

# sqlalchemy db config
app.config["SQLALCHEMY_DATABASE_URI"] = dbUrl
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# psycopg2 db config
urllib.parse.uses_netloc.append("postgres")
url = urllib.parse.urlparse(dbUrl)
dbConnection = psycopg2.connect(database=url.path[1:],
                                user=url.username,
                                password=url.password,
                                host=url.hostname,
                                port=url.port)
