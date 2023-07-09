"""first

Revision ID: 4a4292939350
Revises: 2df01e536d58
Create Date: 2023-07-09 15:58:04.376085

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a4292939350'
down_revision = '2df01e536d58'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member_address',
    sa.Column('member_num', sa.Integer(), nullable=False),
    sa.Column('member_default_address', sa.String(length=256), nullable=False),
    sa.Column('member_address_1', sa.String(length=256), nullable=False),
    sa.Column('member_address_2', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['member_num'], ['shop_members.member_num'], ),
    sa.PrimaryKeyConstraint('member_num')
    )
    op.create_table('shop_point_histories',
    sa.Column('point_history_num', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('member_num', sa.Integer(), nullable=False),
    sa.Column('point_update_date', sa.DateTime(), nullable=False),
    sa.Column('point_status', sa.Boolean(), nullable=False),
    sa.Column('point_use_amount', sa.Integer(), nullable=False),
    sa.Column('point_content', sa.String(length=1), nullable=False),
    sa.ForeignKeyConstraint(['member_num'], ['shop_members.member_num'], ),
    sa.PrimaryKeyConstraint('point_history_num')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_point_histories')
    op.drop_table('member_address')
    # ### end Alembic commands ###