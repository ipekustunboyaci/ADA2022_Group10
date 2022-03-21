"""Create couriers table

Revision ID: 08648eda3922
Revises: f2db6bc1466b
Create Date: 2022-03-21 17:50:24.925476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08648eda3922'
down_revision = 'f2db6bc1466b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'couriers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('store_id', sa.Integer(), sa.ForeignKey('stores.id')),
        sa.Column('status', sa.String())
    )


def downgrade():
    op.drop_table('couriers')