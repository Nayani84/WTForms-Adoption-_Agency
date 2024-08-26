from unittest import TestCase

from app import app
from models import db, Pet

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class PetModelTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self):
        """Clean up any existing users."""

        Pet.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()




