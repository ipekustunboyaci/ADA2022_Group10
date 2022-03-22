from faker import Faker
from . import models

from sqlalchemy.orm import Session

fake = Faker()


def create_product(db: Session):
    db_product = models.Product(
        name=fake.word(),
        description=fake.paragraph(3, variable_nb_sentences = True),
        price=fake.random_int(min=29)
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

