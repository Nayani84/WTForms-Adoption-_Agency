from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = 'https://cdn-icons-png.flaticon.com/512/10453/10453654.png'

"""Models for Pet_Adoption."""
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(50), nullable=False)

    species = db.Column(db.String(50), nullable=False)

    photo_url = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)

    age = db.Column(db.Integer, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    available = db.Column(db.Boolean, nullable=False, default=True)



    def __repr__(self):
        p = self
        return f"<pet id={p.id} name={p.name} species={p.species} photo_url={p.photo_url} age={p.age} notes={p.notes} available={p.available}>"


    def format_available(self):
        """formats the true false for the available boolean column to a friendly string """
        if self.available ==True:
            return "is available for adoption!!"
        else:
            return "has been adopted please look for another pet."

