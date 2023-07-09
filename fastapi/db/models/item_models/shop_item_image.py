from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean, Text
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Item_Images_Model(Base):
    """Model for shop_item_image."""

    __tablename__ = "shop_item_image"
    
    item_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_items.item_num"), primary_key=True) # 상품번호
    item_img_path: Mapped[str] = mapped_column(String(length=256))										# 이미지경로
    