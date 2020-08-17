from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, URL, AnyOf

class PetForm(FlaskForm):

  name = StringField("Pet Name", validators=[DataRequired()])

  species = StringField("Species", validators=[DataRequired(), AnyOf(["cat", "dog", "porcupine"], message="Invalid species. Must be 'cat', 'dog', or 'porcupine'")])

  photo_url = StringField("Photo URL", validators=[DataRequired(), URL()])

  age = IntegerField("Age", validators=[DataRequired(message="Please enter number")])

  notes = TextAreaField("Additional Information")