from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
import os

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Define users schema
users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(50)),
    Column('email', String(50)),
    Column('street_name', String(250)),
    Column('street_number', Integer),
    Column('city_name', String(50)),
    Column('country_name', String(50)),
)

database = Database(DATABASE_URL)