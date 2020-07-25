"""empty message

Revision ID: 06457a539656
Revises: d89d6e60585b
Create Date: 2020-07-24 22:58:33.342806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06457a539656'
down_revision = 'd89d6e60585b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuario', 'fecha',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('usuario', 'nombre',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('usuario', 'nombre',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('usuario', 'fecha',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
