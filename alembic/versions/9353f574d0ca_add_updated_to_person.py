"""add updated to person

Revision ID: 9353f574d0ca
Revises: 4db199799c54
Create Date: 2020-04-13 14:26:03.628437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9353f574d0ca'
down_revision = '4db199799c54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('updated', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'updated')
    # ### end Alembic commands ###
