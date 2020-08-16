from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)

# Models
class Pet(db.Model):

  __tablename__ = "pets"

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)

  name = db.Column(db.Text, nullable=False)

  species = db.Column(db.Text, nullable=False)

  photo_url = db.Column(db.Text, default="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/240px-No_image_available.svg.png")

  age = db.Column(db.Integer)

  notes = db.Column(db.Text)

  available = db.Column(db.Boolean, nullable=False, default=True)