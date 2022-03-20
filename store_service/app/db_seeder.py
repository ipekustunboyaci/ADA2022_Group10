from faker import Faker
from . import models

from sqlalchemy.orm import Session

fake = Faker()


def create_store(db: Session):
    lat, lon = fake.local_latlng(country_code='NL', coords_only = True)
    db_store = models.Store(
        name=fake.company(),
        description=fake.paragraph(3, variable_nb_sentences = True),
        latitude=lat,
        longitude=lon
    )
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

