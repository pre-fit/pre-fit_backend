import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Review_Image_Model(Base):
    """Model for review_image."""

    __tablename__ = "review_image"
    
    review_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_reviews.review_num"), primary_key=True) 	# 리뷰번호  
    item_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_items.item_num"))							# 주문상품번호
    review_img_path: Mapped[str] = mapped_column(String(length=256))											# 리뷰사진
