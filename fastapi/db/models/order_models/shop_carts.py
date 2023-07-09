import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Carts_Model(Base):
    """Model for shop_carts."""

    __tablename__ = "shop_carts"
    
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_items.item_num"), primary_key=True) 	# 회원번호    
    item_option_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_item_options.item_option_num"))	# 옵션번호
