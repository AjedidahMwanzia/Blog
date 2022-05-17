"""second migration

Revision ID: ea55c2a1637c
Revises: 8aaef03bfcb7
Create Date: 2022-05-16 20:42:06.915485

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea55c2a1637c'
down_revision = '8aaef03bfcb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    op.drop_table('upvotes')
    op.drop_table('downvotes')
    op.add_column('pitches', sa.Column('content', sa.Text(), nullable=False))
    op.drop_index('ix_pitches_category', table_name='pitches')
    op.drop_column('pitches', 'post')
    op.drop_column('pitches', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.add_column('pitches', sa.Column('post', sa.TEXT(), autoincrement=False, nullable=False))
    op.create_index('ix_pitches_category', 'pitches', ['category'], unique=False)
    op.drop_column('pitches', 'content')
    op.create_table('downvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='downvotes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='downvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='downvotes_pkey')
    )
    op.create_table('upvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='upvotes_pitch_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='upvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='upvotes_pkey')
    )
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.drop_table('subscribers')
    # ### end Alembic commands ###