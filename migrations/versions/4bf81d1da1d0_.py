"""empty message

Revision ID: 4bf81d1da1d0
Revises: eb33f32c33c4
Create Date: 2017-04-08 10:05:37.239483

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4bf81d1da1d0'
down_revision = 'eb33f32c33c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('content', sa.String(length=100), nullable=True))
    op.drop_column('todos', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('body', mysql.VARCHAR(length=100), nullable=True))
    op.drop_column('todos', 'content')
    # ### end Alembic commands ###
