from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean, Text
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Items_Categories_Model(Base):
    """Model for shop_items_categories."""

    __tablename__ = "shop_item_categories"
    
    item_category_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 	# 카테고리번호    
    item_category_main_name: Mapped[str] = mapped_column(String(length=20))							# 메인카테고리명 
    item_ctegory_sub_name: Mapped[str] = mapped_column(String(length=20))							# 서브카테고리명
    