"""1234

Revision ID: 1fc50670b8f1
Revises: 29eeb07e407e
Create Date: 2022-12-25 20:47:17.259338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fc50670b8f1'
down_revision = '29eeb07e407e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addproduct', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gender', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
