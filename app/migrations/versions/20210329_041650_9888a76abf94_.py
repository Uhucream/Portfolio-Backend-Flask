"""empty message

Revision ID: 9888a76abf94
Revises: 55b2cf7b119f
Create Date: 2021-03-29 04:16:50.652475

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9888a76abf94'
down_revision = '55b2cf7b119f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_works',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('endpoint_uri', sa.Text(), nullable=False),
    sa.Column('top_page_outline', sa.Text(), nullable=False),
    sa.Column('work_url', sa.Text(), nullable=True),
    sa.Column('work_picture_url', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('endpoint_uri'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('my_works')
    # ### end Alembic commands ###
