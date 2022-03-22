"""create products table

Revision ID: 32217927ca83
Revises: 
Create Date: 2022-03-19 15:03:09.639489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32217927ca83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('price', sa.Integer(), nullable=False)
    )


def downgrade():
    op.drop_table('products')
