"""first

Revision ID: 196b5b9525b3
Revises: c323e2d70744
Create Date: 2023-07-09 21:29:38.334436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "196b5b9525b3"
down_revision = "c323e2d70744"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "review_image",
        sa.Column("review_num", sa.Integer(), nullable=False),
        sa.Column("item_num", sa.Integer(), nullable=False),
        sa.Column("review_img_path", sa.String(length=256), nullable=False),
        sa.ForeignKeyConstraint(
            ["item_num"],
            ["shop_items.item_num"],
        ),
        sa.ForeignKeyConstraint(
            ["review_num"],
            ["shop_reviews.review_num"],
        ),
        sa.PrimaryKeyConstraint("review_num"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("review_image")
    # ### end Alembic commands ###
