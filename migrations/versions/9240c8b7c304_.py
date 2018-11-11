"""empty message

Revision ID: 9240c8b7c304
Revises: 
Create Date: 2018-11-11 19:11:26.023411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9240c8b7c304'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('conteudo', sa.Column('imagem', sa.String(length=250), nullable=True))
    op.add_column('conteudo', sa.Column('tema', sa.String(length=250), nullable=True))
    op.add_column('conteudo', sa.Column('tipo_conteudo', sa.String(length=250), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('conteudo', 'tipo_conteudo')
    op.drop_column('conteudo', 'tema')
    op.drop_column('conteudo', 'imagem')
    # ### end Alembic commands ###
