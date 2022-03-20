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

    for x in range(fake.random_int(min = 20, max=300)):
        db_store.inventory.append(
            models.Item(
                reservation=fake.date_time_this_month(),
                product_id=fake.random_int(min=0, max=19)
            )
        )

    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

