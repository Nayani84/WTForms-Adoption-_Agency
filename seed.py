"""Seed file to make sample data for pet adoption db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add users
Luna = Pet(
    name="Luna", 
    species="Dog", 
    photo_url="https://www.metlifepetinsurance.com/content/dam/metlifecom/us/metlifepetinsurance/images/blog/Thumbnails/breed-spotlight/shih-tzu-poodle-thumbnail.webp",
    age=2,
    notes="Shih-poo",
    available=True
    )

Leo = Pet(
    name="Leo", 
    species="Dog", 
    photo_url="https://images.squarespace-cdn.com/content/v1/625ee79ee923a609e4bf10fa/623cc7ef-8b4c-426d-8598-6abba9705b73/BrainSpin_hyper-realistic_photo_of_a_Maltipoo_laying_on_the_gra_684cb0be-885e-41f2-b723-67a9dfa12c26.png",
    age=2,
    notes="Maltipoo",
    available=True
)

Panda = Pet(
    name="Panda", 
    species="Dog", 
    photo_url="https://as1.ftcdn.net/v2/jpg/00/55/43/16/1000_F_55431653_3PDP9tKwEVksvw82sekUMONyPsSi6Qy0.jpg",
    age=13,
    notes="Golden Retriever",
    available=True
)

Binkey = Pet(
    name="Binkey", 
    species="Dog", 
    photo_url="https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-07/Pomeranian.jpg?itok=BGe-1DFz",
    age=15,
    notes="Pomeranian",
    available=False
)

Boola = Pet(
    name="Boola", 
    species="Dog", 
    photo_url="https://media.istockphoto.com/id/513133900/photo/golden-retriever-sitting-in-front-of-a-white-background.jpg?s=612x612&w=0&k=20&c=rPuBgfn_wcAzaa8o2GhrA2eBTdbvrTvYw4demzV-bOs=",
    age=10,
    notes="Labrador",
    available=False
)

Shadow = Pet(
    name="Shadow", 
    species="Cat", 
    photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/George%2C_a_perfect_example_of_a_tuxedo_cat.jpg/220px-George%2C_a_perfect_example_of_a_tuxedo_cat.jpg",
    age=2,
    notes="American Shorthair",
    available=True
)

Mickey = Pet(
    name="Mickey", 
    species="Cat", 
    photo_url="https://cdn-prd.content.metamorphosis.com/wp-content/uploads/sites/2/2022/05/black-and-white-cat-breeds-main.jpg",
    age=1,
    notes="Birman",
    available=True
)

Blacky = Pet(
    name="Blacky", 
    species="Cat", 
    photo_url="https://image.petmd.com/files/inline-images/black-cat-breeds-manx.jpg?VersionId=r4qTZpY8EBNUMGt4GUI7CI1PVpmr6qul",
    age=4,
    notes="Persian cat",
    available=False
)

Teddy = Pet(
    name="Teddy", 
    species="Porcupine", 
    photo_url="https://townline.org/wp-content/uploads/2023/02/Porcupine.jpg",
    age=5,
    notes="North American Porcupine",
    available=True
)

Buddy = Pet(
    name="Buddy", 
    species="Porcupine", 
    photo_url="https://www.nps.gov/articles/images/20210715_Schoodic_AcadiaTeacherFellows-004.jpg",
    age=7,
    notes="Brazilian porcupine",
    available=False
)

# Add new objects to session, so they'll persist
db.session.add_all([Luna, Leo, Panda, Binkey, Boola, Shadow, Mickey, Blacky, Teddy, Buddy])

# Commit--otherwise, this never gets saved!
db.session.commit()

