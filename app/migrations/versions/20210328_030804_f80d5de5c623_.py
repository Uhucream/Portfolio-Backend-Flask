"""empty message

Revision ID: f80d5de5c623
Revises: 55b2cf7b119f
Create Date: 2021-03-28 03:08:04.181683

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f80d5de5c623'
down_revision = '55b2cf7b119f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_works',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('work_name', sa.Text(), nullable=False),
    sa.Column('work_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_works')
    # ### end Alembic commands ###
