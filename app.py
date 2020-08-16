from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)

# Configure and Initialize Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# Configure Debug Toolbar
app.config['SECRET_KEY'] = "cookies"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_home_route():
  pets = Pet.query.all()
  return render_template("pets.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
  form = PetForm()
  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    url = form.photo_url.data 
    age = form.age.data
    notes = form.notes.data
    # flash(f"Created new snack: name is {name}, price is {price}")
    new_pet = Pet(name=name, species=species, photo_url=url, age=age, notes=notes)
    db.session.add(new_pet)
    db.session.commit()
    return redirect("/")
  else:
    return render_template("add_form.html", form=form)