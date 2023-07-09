from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Point_Histories_Model(Base):
    """Model for shop_point_histories."""

    __tablename__ = "shop_point_histories"
    
    point_history_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 	# 포인트번호
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num")) 		# 회원번호    
    point_update_date: Mapped[str] = mapped_column(DateTime)										# 포인트이력날짜
    point_status: Mapped[str] = mapped_column(Boolean)												# 포인트상태이력(적립, 사용)
    point_use_amount: Mapped[str] = mapped_column(Integer)											# 포인트사용량
    point_content: Mapped[str] = mapped_column(String(length=1))									# 포인트발생이유(구매, 사용, 이벤트 등)
    