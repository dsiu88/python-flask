"""followers

Revision ID: 41784699a1f8
Revises: 99fdf3948710
Create Date: 2018-10-05 11:30:51.134729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41784699a1f8'
down_revision = '99fdf3948710'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
