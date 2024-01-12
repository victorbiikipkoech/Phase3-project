"""create_city_and_weather_data_tables

Revision ID: a59b88d405fe
Revises: 2e190eb07ae6
Create Date: 2024-01-11 12:38:13.602163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a59b88d405fe'
down_revision: Union[str, None] = '2e190eb07ae6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
