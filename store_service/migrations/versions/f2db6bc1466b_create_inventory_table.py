"""Create Inventory table

Revision ID: f2db6bc1466b
Revises: 0f958d149f9e
Create Date: 2022-03-20 18:46:20.815435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2db6bc1466b'
down_revision = '0f958d149f9e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'inventory',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('product_id', sa.Integer()),
        sa.Column('store_id', sa.Integer(), sa.ForeignKey('stores.id')),
        sa.Column('reservation', sa.DateTime())
    )


def downgrade():
    pass
