"""first

Revision ID: 0662a3d9accc
Revises: 88003fcbbf5a
Create Date: 2023-07-09 21:08:55.907838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0662a3d9accc"
down_revision = "88003fcbbf5a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "shop_orders",
        sa.Column("order_num", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("member_num", sa.Integer(), nullable=False),
        sa.Column("order_create_date", sa.DateTime(), nullable=False),
        sa.Column("order_pyment_status", sa.String(length=15), nullable=False),
        sa.Column("order_pyment_method", sa.String(length=15), nullable=False),
        sa.Column("order_total_price", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["member_num"],
            ["shop_members.member_num"],
        ),
        sa.PrimaryKeyConstraint("order_num"),
    )
    op.create_table(
        "shop_order_products",
        sa.Column(
            "order_product_num", sa.Integer(), autoincrement=True, nullable=False
        ),
        sa.Column("item_option_num", sa.Integer(), nullable=False),
        sa.Column("order_num", sa.Integer(), nullable=False),
        sa.Column("member_num", sa.Integer(), nullable=False),
        sa.Column("order_amount", sa.Integer(), nullable=False),
        sa.Column("review_enabled", sa.Boolean(), nullable=False),
        sa.Column("order_status", sa.String(length=15), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_option_num"],
            ["shop_item_options.item_option_num"],
        ),
        sa.ForeignKeyConstraint(
            ["member_num"],
            ["shop_members.member_num"],
        ),
        sa.ForeignKeyConstraint(
            ["order_num"],
            ["shop_orders.order_num"],
        ),
        sa.PrimaryKeyConstraint("order_product_num"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("shop_order_products")
    op.drop_table("shop_orders")
    # ### end Alembic commands ###
