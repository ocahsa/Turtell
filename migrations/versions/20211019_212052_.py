"""empty message

Revision ID: bfdf28c5fd2a
Revises: 4798e0efd860
Create Date: 2021-10-19 21:20:52.423915

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfdf28c5fd2a'
down_revision = '4798e0efd860'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('subreddit_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subreddit_id'], ['subreddits.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('members')
    # ### end Alembic commands ###
