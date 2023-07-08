from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Member_Address_Model(Base):
    """Model for demo purpose."""

    __tablename__ = "member_address"
    
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num"), primary_key=True) 	# 회원번호
    member_default_address: Mapped[str] = mapped_column(String(length=256))						# 기본 주소지
    member_address_1: Mapped[str] = mapped_column(String(length=256))							# 주소지1
    member_address_2: Mapped[str] = mapped_column(String(length=256))							# 주소지2