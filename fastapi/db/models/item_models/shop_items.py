from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean, Text
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Items_Model(Base):
    """Model for shop_items."""

    __tablename__ = "shop_items"
    
    item_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 							# 상품번호    
    item_category_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_item_categories.item_category_num"))	# 카테고리번호    
    item_name: Mapped[str] = mapped_column(String(length=20))														# 상품명
    item_description: Mapped[str] = mapped_column(Text)																# 상품설명
    item_price: Mapped[str] = mapped_column(Integer)																# 상품가격
    item_discount_price: Mapped[str] = mapped_column(Integer)														# 상품할인가격
    item_create_date: Mapped[str] = mapped_column(DateTime)															# 상품등록일
    item_soldout: Mapped[str] = mapped_column(Boolean)																# 품절여부
    