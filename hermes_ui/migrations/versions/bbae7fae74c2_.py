"""empty message

Revision ID: bbae7fae74c2
Revises: eccb7efb059f
Create Date: 2019-07-15 11:12:58.328298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbae7fae74c2'
down_revision = 'eccb7efb059f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('localisation_expression_recherche_interet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('expression_gauche', sa.String(), nullable=False),
    sa.Column('expression_droite', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['recherche_interet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('localisation_expression_recherche_interet')
    # ### end Alembic commands ###
