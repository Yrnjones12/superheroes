import os
from app import db  
from models import Hero, HeroPower, Power
from datetime import datetime
import random
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.app_context().push()

# Generate powers data
power1 = Power(name="Super Strength", description="Grants super-human strength")
power2 = Power(name="Flight", description="Enables the ability to fly at supersonic speed")
power3 = Power(name="Superhuman Senses", description="Enhances senses to a super-human level")

# Generate heroes data
heroes_data = [
  {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
  {"name": "Doreen Green", "super_name": "Squirrel Girl"},
  {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
  {"name": "Janet Van Dyne", "super_name": "The Wasp"},
  {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
  {"name": "Carol Danvers", "super_name": "Captain Marvel"},
  {"name": "Jean Grey", "super_name": "Dark Phoenix"},
  {"name": "Ororo Munroe", "super_name": "Storm"},
  {"name": "Kitty Pryde", "super_name": "Shadowcat"},
  {"name": "Elektra Natchios", "super_name": "Elektra"}
]

heroes = [Hero(name=data["name"], super_name=data["super_name"], created_at=datetime.utcnow(), updated_at=datetime.utcnow()) for data in heroes_data]

# Generate hero powers data
strengths = ["Strong", "Weak", "Average"]

# Seed the HeroPower table
for hero in heroes:
  for n in range(random.randint(1, 3)):
    power = random.choice([power1, power2, power3])
    strength = random.choice(strengths)
    hero_power = HeroPower(hero=hero, power=power, strength=strength, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
    db.session.add(hero_power)

# Commit the changes to the database
db.session.commit()

print("Done seeding!")

if __name__ == '__main__':
  app.run(port=5555)