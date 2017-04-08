"""empty message

Revision ID: 680a8b2fcd9d
Revises: 4ddd55c0db60
Create Date: 2017-04-06 12:08:59.665117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '680a8b2fcd9d'
down_revision = '4ddd55c0db60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('collect',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_collect_created'), 'collect', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_collect_created'), table_name='collect')
    op.drop_table('collect')
    # ### end Alembic commands ###
