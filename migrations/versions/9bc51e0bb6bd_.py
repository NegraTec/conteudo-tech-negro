"""empty message

Revision ID: 9bc51e0bb6bd
Revises: 9240c8b7c304
Create Date: 2018-11-17 14:40:53.258466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bc51e0bb6bd'
down_revision = '9240c8b7c304'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('user', 'password',
                    existing_type=sa.String(length=64),
                    type_=sa.String(length=150))


def downgrade():
    op.alter_column('user', 'password',
                    existing_type=sa.String(length=150),
                    type_=sa.String(length=64))
