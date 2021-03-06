"""Create model tables for user, category, pitch, upvote and downvote

Revision ID: 96f80b9e6f8d
Revises: 1d191f98c116
Create Date: 2020-07-14 02:43:25.845248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96f80b9e6f8d'
down_revision = '1d191f98c116'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pitch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=1000), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('downvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('upvote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pitch_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitch.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('email', sa.String(length=80), nullable=True))
    op.alter_column('user', 'f_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('user', 'l_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.create_unique_constraint(None, 'user', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.alter_column('user', 'l_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('user', 'f_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_column('user', 'email')
    op.drop_table('upvote')
    op.drop_table('downvote')
    op.drop_table('pitch')
    op.drop_table('category')
    # ### end Alembic commands ###
