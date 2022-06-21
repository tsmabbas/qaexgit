from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

db.create_all()


@app.route('/')
def home():
    return "This is from the webserver Hello Internet"

@app.route('/about', methods=['GET', 'POST'])
def about():
    return "this is about page"

@app.route('/about/steve')
def aboutsteve():
    return "this is about Steve"

@app.route('/calc/<int:num>')
def calc(num):
    return str(num * 5)

@app.route('/goog')
def goog():
    return redirect("https://www.google.com")


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port =5000)

