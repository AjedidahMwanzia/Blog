"""update models.py

Revision ID: 3aeaf7f2275e
Revises: ea55c2a1637c
Create Date: 2022-05-16 20:44:24.388723

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3aeaf7f2275e'
down_revision = 'ea55c2a1637c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    op.drop_column('pitches', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'posted')
    # ### end Alembic commands ###