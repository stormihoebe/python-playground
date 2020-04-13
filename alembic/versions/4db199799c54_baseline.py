"""baseline

Revision ID: 4db199799c54
Revises: 
Create Date: 2020-04-13 12:13:57.920779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4db199799c54'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'person',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String()),
        sa.Column('age', sa.Integer)
    )


def downgrade():
    op.drop_table(
        'person'
    )
