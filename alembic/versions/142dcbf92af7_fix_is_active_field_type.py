"""Fix is_active field type

Revision ID: 142dcbf92af7
Revises: ff69366f82aa
Create Date: 2024-06-19 15:20:28.316369

"""
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = '142dcbf92af7'
down_revision: Union[str, None] = 'ff69366f82aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###