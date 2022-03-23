from faker import Faker
from . import models, schemas

from sqlalchemy.orm import Session

fake = Faker()
# Create fake data for inventory to allow operations


def create_inventory(db: Session, n: int):

    db_items = [models.Item(
            product_name=fake.word(),
            count=fake.random_int(),
            price=fake.random_int(min=29),
            store_id=fake.random_int(min=1, max=20)
        ) for x in range(n)]
    db.bulk_save_objects(db_items)
    db.commit()

    return db_items

