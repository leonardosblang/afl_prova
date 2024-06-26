"""Add trade_name to companies

Revision ID: 3fda536f17fc
Revises: 142dcbf92af7
Create Date: 2024-06-19 18:37:10.462695

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '3fda536f17fc'
down_revision: Union[str, None] = '142dcbf92af7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('trade_name', sa.String(), nullable=True))
    op.create_index(op.f('ix_companies_trade_name'), 'companies', ['trade_name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_companies_trade_name'), table_name='companies')
    op.drop_column('companies', 'trade_name')
    # ### end Alembic commands ###
