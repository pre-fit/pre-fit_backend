"""first

Revision ID: 73567e151a44
Revises: 2b7380507a71
Create Date: 2023-07-08 20:34:29.345324

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '73567e151a44'
down_revision = '2b7380507a71'
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
    sa.Column('member_gender', sa.String(length=1), nullable=False),
    sa.Column('member_birthday', sa.DateTime(), nullable=False),
    sa.Column('member_point', sa.Integer(), nullable=False),
    sa.Column('member_email', sa.String(length=256), nullable=False),
    sa.Column('member_grade', sa.Integer(), nullable=False),
    sa.Column('member_join_date', sa.DateTime(), nullable=False),
    sa.Column('member_leave_date', sa.DateTime(), nullable=False),
    sa.Column('member_join_falg', sa.String(length=1), nullable=False),
    sa.Column('member_active', sa.String(length=1), nullable=False),
    sa.Column('member_terms_of_service', sa.String(length=1), nullable=False),
    sa.Column('member_privacy_policy', sa.String(length=1), nullable=False),
    sa.Column('member_recive_marketing_info', sa.String(length=1), nullable=False),
    sa.Column('member_approve', sa.String(length=1), nullable=False),
    sa.Column('member_recommender', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('member_num')
    )
    op.alter_column('dummy_model', 'name',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dummy_model', 'name',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.drop_table('shop_members')
    # ### end Alembic commands ###
