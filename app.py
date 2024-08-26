"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
from forms import AddPetForm, EditPetForm
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'abcde'
debug=DebugToolbarExtension(app)

app.app_context().push()
app.app_context()

connect_db(app)
db.create_all()

@app.route('/')
def home():
    """home page. Pet list"""

    pets = Pet.query.all()

    return render_template("pet_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """show add pet form and handle the form."""
    pet_form = AddPetForm()

    if pet_form.validate_on_submit():
        pet_name = pet_form.name.data
        pet_species = pet_form.species.data
        pet_photo_url = pet_form.photo_url.data
        pet_age = pet_form.age.data
        pet_notes = pet_form.notes.data
        pet_available = pet_form.available.data

        flash(f"Added name={pet_name} species={pet_species} age= {pet_age} notes={pet_notes} photo_url={pet_photo_url}")

        new_pet=Pet(name=pet_name, species=pet_species, photo_url=pet_photo_url, age=pet_age, notes=pet_notes, available=pet_available)
        db.session.add(new_pet)
        db.session.commit()
        flash("New pet created!!")

        return redirect("/")
    else:
        return render_template("create_pet.html", pet_form=pet_form)


@app.route("/<int:pet_id>" , methods=["GET", "POST"])
def show_pet(pet_id):
    """Show info on a single pet and edit pet details."""

    pet = Pet.query.get_or_404(pet_id)
    pet_form = EditPetForm(obj=pet)

    if pet_form.validate_on_submit():
        pet.photo_url = pet_form.photo_url.data
        pet.notes = pet_form.notes.data
        pet.available = pet_form.available.data
       
        db.session.commit()
        flash(f"{pet.name} has been updated!!")
        return redirect("/")
    else:
        return render_template("pet_detail_edit.html", pet_form=pet_form, pet=pet)




