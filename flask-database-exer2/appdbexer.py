
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password@34.142.44.27:3306/mohammed"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello_internet():
    return "Hello Internet"

if __name__ == "__main__":
    app.run(debug=True)
