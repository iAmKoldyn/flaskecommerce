"""1234

Revision ID: 7755ab59ebeb
Revises: bde013ec0760
Create Date: 2022-12-25 21:15:20.872483

"""
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision = '7755ab59ebeb'
down_revision = 'bde013ec0760'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addproduct', schema=None) as batch_op:
        batch_op.add_column(sa.Column('size', sa.Integer(), nullable=False, server_default="0"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addproduct', schema=None) as batch_op:
        batch_op.drop_column('size')

    # ### end Alembic commands ###
