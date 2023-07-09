import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Item_Options_Model(Base):
    """Model for shop_item_options."""

    __tablename__ = "shop_item_options"
    
    item_option_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) # 옵션번호    
    item_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_items.item_num"))			# 상품번호
    item_option_color: Mapped[str] = mapped_column(String(length=10))							# 상품색상
    item_option_size: Mapped[str] = mapped_column(String(length=5))								# 상품사이즈
    item_option_soldout: Mapped[bool] = mapped_column(Boolean)									# 옵션별 상품 판매여부
    item_option_is_discount: Mapped[bool] = mapped_column(Boolean)								# 할인여부
    item_option_discount_price: Mapped[int] = mapped_column(Integer)							# 할인가격
    item_option_discount_start_date: Mapped[datetime] = mapped_column(DateTime)		# 할인시작일
    item_option_discount_end_date: Mapped[datetime] = mapped_column(DateTime)			# 할인종료일
