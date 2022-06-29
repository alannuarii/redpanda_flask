"""empty message

Revision ID: a6f2b21d46c8
Revises: 45d885ee4d84
Create Date: 2022-06-27 17:51:45.514681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6f2b21d46c8'
down_revision = '45d885ee4d84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feeder', sa.Column('pltd_tahuna', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('feeder', 'pltd_tahuna')
    # ### end Alembic commands ###
