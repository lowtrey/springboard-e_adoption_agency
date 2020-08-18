from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, URL, AnyOf, NumberRange

class PetForm(FlaskForm):

  name = StringField("Pet Name", validators=[DataRequired()])

  species = StringField("Species", validators=[DataRequired(), AnyOf(["cat", "dog", "porcupine"], message="Invalid species. Must be 'cat', 'dog', or 'porcupine'")])

  photo_url = StringField("Photo URL", validators=[DataRequired(), URL()])

  age = IntegerField("Age", validators=[DataRequired(message="Please enter age"), NumberRange(min=0, max=30, message="Age must be between 0 and 30")])

  notes = TextAreaField("Additional Information")

  is_available = BooleanField("Available for adoption?")