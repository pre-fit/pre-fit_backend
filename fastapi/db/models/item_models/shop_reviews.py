import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Reviews_Model(Base):
    """Model for shop_reviews."""

    __tablename__ = "shop_reviews"
    
    review_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 							# 리뷰번호  
    order_product_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_order_products.order_product_num"))	# 주문상품번호
    item_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_items.item_num"))								# 상품번호
    review_star: Mapped[int] = mapped_column(Integer)																# 리뷰별점
    review_title: Mapped[str] = mapped_column(String(length=128))													# 리뷰제목
    review_contents: Mapped[str] = mapped_column(String(length=512))												# 리뷰내용
    review_create_date: Mapped[datetime] = mapped_column(DateTime)													# 리뷰날짜
    review_image: Mapped[str] = mapped_column(String(length=256))													# 리뷰사진
