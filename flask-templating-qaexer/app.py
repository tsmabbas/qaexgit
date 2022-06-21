# Import everything we need
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from flask_testing import TestCase
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = "SECRET_KEY" # Should be passed as env variable
db = SQLAlchemy(app) # Declare SQLAlchemy object




class Owners(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)


class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cities = db.relationship('Cities', backref='country') 
    borough = db.relationship('Borough', backref='borough') 

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)


class Borough(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)


class OwnerForm(FlaskForm):
    first_name = StringField("First Name: ", validators=[DataRequired(), Length(min=2, max=15)])
    last_name = StringField("Last Name: ")
    submit = SubmitField("Submit")

    def validate_first_name(self, first_name):
        if first_name.data.lower() == "admin" or first_name.data.lower() == "administrator":
            raise ValidationError("First name cannot be 'Admin'")

class TestBase(TestCase):
    def create_app(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    
#     list_of_owners = Owners.query.all()
#     return_string = ""
#     for owner in list_of_owners:
#         #return_string += owner.first_name
#         name = owner.first_name + "  " + owner.last_name 
#         return_string += name # + "\n"

#     # return '\n'.join(return_string)
#     return render_template('index.html', list1=list_of_owners)

@app.route('/')
def homePage():
    list_of_owners = Owners.query.all()
    return render_template('index.html', list1=list_of_owners)
    
@app.route('/add-owner', methods=["GET", "POST"])
def add_owner():
    form = OwnerForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            new_entry = Owners(first_name=form.first_name.data, last_name=form.last_name.data)
            db.session.add(new_entry)
            db.session.commit()
            return redirect(url_for('homePage'))
            

    return render_template('add_owner.html', form=form)


@app.route('/delete/<int:id>',methods=["GET"])
def delete(id):
    deleted_item = Owners.query.get(id)
    db.session.delete(deleted_item)
    db.session.commit()
    return redirect(url_for('homePage'))

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = OwnerForm()

    if request.method =='POST':
        updated_item = Owners.query.get(id)
        updated_item.first_name = form.first_name.data
        updated_item.last_name = form.last_name.data
    db.session.commit()
    return redirect(url_for('home'))

    return render_template('add_owner.html', form=form)

# class DogForm(FlaskForm):
#     name = StringField("Name : " )
#     age = IntegerField("Age : ")
#     breed = SelectField("Breed : ", choices=[("collie", "Collie"),("retriever","Retriever")])
#     submit = SubmitField("submit")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


