"""add llm answer table

Revision ID: 88a8b1b0f340
Revises: f0b7ad62828b
Create Date: 2024-11-29 18:49:32.323025

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "88a8b1b0f340"
down_revision: Union[str, None] = "f0b7ad62828b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "llmanswers",
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("answer", sa.Text(), nullable=False),
        sa.Column("uid", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("uid"),
    )
    op.add_column(
        "products", sa.Column("uid", sa.Integer(), autoincrement=True, nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("products", "uid")
    op.drop_table("llmanswers")
    # ### end Alembic commands ###
