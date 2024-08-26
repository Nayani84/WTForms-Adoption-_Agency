from unittest import TestCase

from app import app
from models import db, Pet

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

app.app_context().push()
app.app_context()

db.drop_all()
db.create_all()


class PetViewsTestCase(TestCase):
    """Tests for views for Pets."""

    def setUp(self):
        """Add sample user."""
        Pet.query.delete()
        
        pet=Pet(name="Rex", species="Dog", photo_url="https://uk.zooexperte.com/image/cache/catalog/Der%20Zoo%20Exsperte/Blog/siberian-husky-hundefutter-und-rasseportrait-w1170-h688.jpg", age=8, notes="Husky", available=True)
        db.session.add(pet)
        db.session.commit()

        self.pet_id = pet.id
        self.pet = pet


    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()


    def test_home_page(self):
        """Check to make sure correct HTML is displayed."""

        with app.test_client() as client:
            resp = client.get('/')
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="ml-3 text-center">Pets</h1>', html)
            
            

    def test_add_pet(self):
        """make sure add pet form page returns and add data handle correctly."""

        with app.test_client() as client:
            data = {
                    "name" :"Dexter",
                     "species" :"Dog", 
                     "photo_url" :"https://uk.zooexperte.com/image/cache/catalog/Der%20Zoo%20Exsperte/Blog/siberian-husky-hundefutter-und-rasseportrait-w1170-h688.jpg",
                     "age" :9,
                     "notes" : "Husky"
                    }

            resp = client.post("/add", data=data, follow_redirects=True)
            html=resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="ml-3">Create a new pet</h1>',html)
            self.assertIn(b'Dexter', resp.data)

