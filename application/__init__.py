from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hnleevfk:HNQ4OnE7b3OGHfYh8x-dwOKakgwj5HKQ@trumpet.db.elephantsql.com/hnleevfk'
db = SQLAlchemy(app)

from application import routes