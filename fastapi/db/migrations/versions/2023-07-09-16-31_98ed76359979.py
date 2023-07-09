"""first

Revision ID: 98ed76359979
Revises: f164e01304f0
Create Date: 2023-07-09 16:31:49.379501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "98ed76359979"
down_revision = "f164e01304f0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shop_board_categories",
        sa.Column(
            "board_categorie_num", sa.Integer(), autoincrement=True, nullable=False
        ),
        sa.Column("main_board_category_name", sa.String(length=20), nullable=False),
        sa.Column("sub_board_category_name", sa.String(length=20), nullable=False),
        sa.PrimaryKeyConstraint("board_categorie_num"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shop_board_categories")
    # ### end Alembic commands ###