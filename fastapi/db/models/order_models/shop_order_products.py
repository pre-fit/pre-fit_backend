import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Order_Products_Model(Base):
    """Model for shop_item_options."""

    __tablename__ = "shop_order_products"
    
    order_product_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 			# 주문상품번호  
    item_option_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_item_options.item_option_num"))	# 옵션번호
    order_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_orders.order_num"))					# 주문번호
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num"))					# 회원번호
    order_amount: Mapped[int] = mapped_column(Integer)														# 주문수량
    review_enabled: Mapped[bool] = mapped_column(Boolean)													# 리뷰여부
    order_status: Mapped[str] = mapped_column(String(length=15))											# 주문상태
