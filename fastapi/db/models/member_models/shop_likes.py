from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Likes_Model(Base):
    """Model for shop_lises."""

    __tablename__ = "shop_likes"
    
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num"), primary_key=True) 	# 회원번호    
    item_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_items.item_num"))							# 상품번호
    