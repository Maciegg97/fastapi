"""add content column to posts table

Revision ID: 8a5b90ffd96c
Revises: 04b792954d57
Create Date: 2022-10-19 19:48:07.331513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a5b90ffd96c'
down_revision = '04b792954d57'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
