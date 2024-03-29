"""empty message

Revision ID: 8f06466a5ea1
Revises: 
Create Date: 2019-11-22 22:51:44.219105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f06466a5ea1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('world_finals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('winners', sa.String(length=100), nullable=True),
    sa.Column('final_score', sa.String(length=100), nullable=True),
    sa.Column('runners_up', sa.Integer(), nullable=True),
    sa.Column('venue', sa.String(length=100), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('attendance', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('year')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('world_finals')
    # ### end Alembic commands ###
