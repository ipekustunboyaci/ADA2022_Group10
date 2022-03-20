"""create stores table

Revision ID: 0f958d149f9e
Revises: 
Create Date: 2022-03-19 18:08:52.827637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f958d149f9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'stores',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        sa.Column('latitude', sa.Float(6)),
        sa.Column('longitude', sa.Float(6))
    )


def downgrade():
    op.drop_table('stores')
