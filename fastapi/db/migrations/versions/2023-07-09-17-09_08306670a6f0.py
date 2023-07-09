"""first

Revision ID: 08306670a6f0
Revises: 0ee4b585402a
Create Date: 2023-07-09 17:09:42.070620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "08306670a6f0"
down_revision = "0ee4b585402a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shop_item_image",
        sa.Column("item_num", sa.Integer(), nullable=False),
        sa.Column("item_img_path", sa.String(length=256), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_num"],
            ["shop_items.item_num"],
        ),
        sa.PrimaryKeyConstraint("item_num"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shop_item_image")
    # ### end Alembic commands ###