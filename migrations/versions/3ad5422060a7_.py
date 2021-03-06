"""empty message

Revision ID: 3ad5422060a7
Revises: d0ff2f23d725
Create Date: 2016-05-19 00:01:43.633946

"""

# revision identifiers, used by Alembic.
revision = '3ad5422060a7'
down_revision = 'd0ff2f23d725'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reply', sa.UnicodeText(), nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_column('reply')

    ### end Alembic commands ###
