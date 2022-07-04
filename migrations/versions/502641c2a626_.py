"""empty message

Revision ID: 502641c2a626
Revises: 
Create Date: 2022-07-03 11:23:06.266073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '502641c2a626'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feeder',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal', sa.String(length=30), nullable=False),
    sa.Column('jam', sa.String(length=10), nullable=False),
    sa.Column('kota', sa.Integer(), nullable=True),
    sa.Column('tona', sa.Integer(), nullable=True),
    sa.Column('kolongan', sa.Integer(), nullable=True),
    sa.Column('lesabe', sa.Integer(), nullable=True),
    sa.Column('tamako', sa.Integer(), nullable=True),
    sa.Column('mainlinepetta', sa.Integer(), nullable=True),
    sa.Column('pettakota', sa.Integer(), nullable=True),
    sa.Column('mainlinetahuna', sa.Integer(), nullable=True),
    sa.Column('kendahe', sa.Integer(), nullable=True),
    sa.Column('bowongkulu', sa.Integer(), nullable=True),
    sa.Column('kotatamako', sa.Integer(), nullable=True),
    sa.Column('lapango', sa.Integer(), nullable=True),
    sa.Column('tahuna', sa.Integer(), nullable=True),
    sa.Column('salurang', sa.Integer(), nullable=True),
    sa.Column('pintareng', sa.Integer(), nullable=True),
    sa.Column('tahunaincome', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('unit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama_unit', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mesin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('unit', sa.String(length=5), nullable=False),
    sa.Column('nama_mesin', sa.String(length=20), nullable=False),
    sa.Column('daya_mampu', sa.Integer(), nullable=False),
    sa.Column('is_sewa', sa.Boolean(), nullable=False),
    sa.Column('unit_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['unit_id'], ['unit.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('har',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tanggal_jumat', sa.String(length=30), nullable=False),
    sa.Column('jumat', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('sabtu', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('minggu', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('senin', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('selasa', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('rabu', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('kamis', sa.Enum('Standby', 'P0', 'P1', 'P2', 'P3', 'P4', 'P5', 'TO', 'SO', 'MO', 'PdM', 'CM', name='harenum'), nullable=False),
    sa.Column('mesin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mesin_id'], ['mesin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('har')
    op.drop_table('mesin')
    op.drop_table('unit')
    op.drop_table('feeder')
    # ### end Alembic commands ###