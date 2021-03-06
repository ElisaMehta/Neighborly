"""empty message

Revision ID: 6ade7f1e46f9
Revises: 1a38f8501549
Create Date: 2020-04-27 12:34:03.540882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ade7f1e46f9'
down_revision = '1a38f8501549'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('addresses', sa.Column('zipcode', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('addresses', 'zipcode')
    # ### end Alembic commands ###
