"""first

Revision ID: 9806609e4458
Revises: 73567e151a44
Create Date: 2023-07-08 22:37:36.951508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9806609e4458'
down_revision = '73567e151a44'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shop_members',
    sa.Column('member_num', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('member_id', sa.String(length=20), nullable=False),
    sa.Column('member_name', sa.String(length=50), nullable=False),
    sa.Column('member_password', sa.String(length=50), nullable=False),
    sa.Column('member_phone', sa.String(length=20), nullable=False),
    sa.Column('member_gender', sa.Boolean(), nullable=False),
    sa.Column('member_birthday', sa.DateTime(), nullable=False),
    sa.Column('member_point', sa.Integer(), nullable=False),
    sa.Column('member_email', sa.String(length=256), nullable=False),
    sa.Column('member_grade', sa.Integer(), nullable=False),
    sa.Column('member_join_date', sa.DateTime(), nullable=False),
    sa.Column('member_leave_date', sa.DateTime(), nullable=False),
    sa.Column('member_join_falg', sa.Boolean(), nullable=False),
    sa.Column('member_active', sa.Boolean(), nullable=False),
    sa.Column('member_terms_of_service', sa.Boolean(), nullable=False),
    sa.Column('member_privacy_policy', sa.Boolean(), nullable=False),
    sa.Column('member_recive_marketing_info', sa.Boolean(), nullable=False),
    sa.Column('member_approve', sa.Boolean(), nullable=False),
    sa.Column('member_recommender', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('member_num')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_members')
    # ### end Alembic commands ###