"""Add relationship between City and WeatherData

Revision ID: 2e190eb07ae6
Revises: 
Create Date: 2024-01-11 11:27:22.869539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e190eb07ae6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
