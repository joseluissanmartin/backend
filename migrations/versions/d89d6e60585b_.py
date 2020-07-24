"""empty message

Revision ID: d89d6e60585b
Revises: 0fc9fb91a07d
Create Date: 2020-07-22 23:12:48.488931

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd89d6e60585b'
down_revision = '0fc9fb91a07d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('correo', sa.String(), nullable=False),
    sa.Column('fecha', sa.String(), nullable=False),
    sa.Column('sistema_o', sa.String(), nullable=True),
    sa.Column('procesador', sa.String(), nullable=True),
    sa.Column('almacenamiento', sa.String(), nullable=True),
    sa.Column('ram', sa.String(), nullable=True),
    sa.Column('grafica', sa.String(), nullable=True),
    sa.Column('direct_x', sa.String(), nullable=True),
    sa.Column('gusto', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
