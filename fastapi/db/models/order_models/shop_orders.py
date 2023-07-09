import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Orders_Model(Base):
    """Model for shop_item_options."""

    __tablename__ = "shop_orders"
    
    order_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 		# 주문번호    
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num"))		# 회원번호
    order_create_date: Mapped[datetime] = mapped_column(DateTime)								# 주문수량
    order_pyment_status: Mapped[str] = mapped_column(String(length=15))							# 결제상태
    order_pyment_method: Mapped[str] = mapped_column(String(length=15))							# 결제수단
    order_total_price: Mapped[int] = mapped_column(Integer)										# 최종결제금액
