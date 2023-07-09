"""first

Revision ID: 74f887bf8cd2
Revises: 196b5b9525b3
Create Date: 2023-07-09 21:39:24.633764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "74f887bf8cd2"
down_revision = "196b5b9525b3"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "shop_board_comments_ibfk_1", "shop_board_comments", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "shop_board_comments",
        "shop_question_boards",
        ["board_num"],
        ["board_num"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "shop_board_comments", type_="foreignkey")
    op.create_foreign_key(
        "shop_board_comments_ibfk_1",
        "shop_board_comments",
        "shop_board_categories",
        ["board_num"],
        ["board_categorie_num"],
    )
    # ### end Alembic commands ###