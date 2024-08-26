from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL



class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name=StringField("Pet Name", validators=[InputRequired(message="Please add a pet name")])
    species=SelectField("Species", validators=[InputRequired(message="Please choose a species")], choices=[('dog' ,'Dog' ), ('cat' , 'Cat'), ('porcupine' , 'Porcupine')])
    photo_url=StringField("Photo URL", validators=[Optional(), URL(require_tld=False, message="please enter a valid URL for your pets photo")])
    age=IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="choose an age from zero to 30")])
    notes=StringField("Notes", validators=[Optional()])
    available=BooleanField("Available" , validators=[Optional()])



class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url=StringField("Photo URL", validators=[Optional(), URL(require_tld=False, message="please enter a valid URL for your pets photo")])
    notes=StringField("Notes", validators=[Optional()])
    available=BooleanField("Available" , validators=[Optional()])