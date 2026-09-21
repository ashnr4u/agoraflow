"""add role check contraint

Revision ID: dff613311617
Revises: 3b37468d4716
Create Date: 2026-09-21 17:49:55.113910

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dff613311617'
down_revision: Union[str, Sequence[str], None] = '3b37468d4716'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# create checking_roles constraint
def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "checking_roles",
        "users",
        "role IN ('student','organiser')"
    )
# remove checking_roles constraint
def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "checking_roles",
        "users",
        type_="check"
    )