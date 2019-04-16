"""empty message

Revision ID: 642b610cdb7b
Revises: 
Create Date: 2019-04-13 13:42:05.384098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642b610cdb7b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Data_controller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_point', sa.String(), nullable=False),
    sa.Column('description_point', sa.String(), nullable=False),
    sa.Column('value_point', sa.String(), nullable=False),
    sa.Column('time_save', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Data_controller')
    # ### end Alembic commands ###
