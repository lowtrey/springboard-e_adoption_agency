from models import db, Pet
from app import app

# Create All Tables
db.drop_all()
db.create_all()

  # name = db.Column(db.Text, nullable=False)

  # species = db.Column(db.Text, nullable=False)

  # photo_url = db.Column(db.Text)

  # age = db.Column(db.Integer)

  # notes = db.Column(db.Text)

  # available = db.Column(db.Boolean, nullable=False, default=True)

# Add sample pets
benny = Pet(
  name="Benny", 
  species="maltipoo", 
  age=7, 
  notes="Mild mannered, service puppy from a good family.", 
  available=False
  )

taka = Pet(
  name="Taka", 
  species="pit bull", 
  age=15
  )

nemo = Pet(
  name="Nemo", 
  species="fish", 
  photo_url="https://i.pinimg.com/originals/e3/e5/dc/e3e5dc4143d77b3dcea61776d372928c.gif", 
  age=2, 
  notes="World renowned aquatic movie star."
  ) 

porky = Pet(
  name="Porky", 
  species="pig", 
  photo_url="https://upload.wikimedia.org/wikipedia/en/thumb/8/88/Porky_Pig.svg/1200px-Porky_Pig.svg.png", 
  age=30
  )

db.session.add_all([benny, taka, nemo, porky])
db.session.commit()