"""empty message

Revision ID: 9bbcc996d78f
Revises: 
Create Date: 2021-07-11 05:25:50.519984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bbcc996d78f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venues')
    op.drop_table('places')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('places',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pdescription', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], name='places_venue_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='places_pkey')
    )
    op.create_table('venues',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('vname', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='venues_pkey')
    )
    # ### end Alembic commands ###
