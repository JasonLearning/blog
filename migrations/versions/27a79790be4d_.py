"""empty message

Revision ID: 27a79790be4d
Revises: 5fce93ec0c29
Create Date: 2016-09-29 09:07:59.264744

"""

# revision identifiers, used by Alembic.
revision = '27a79790be4d'
down_revision = '5fce93ec0c29'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
   # with op.batch_alter_table('articles', schema=None) as batch_op:
    #    batch_op.create_unique_constraint(None, ['title'])
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('disabled', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    ### end Alembic commands ###
