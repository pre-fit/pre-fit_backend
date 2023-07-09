from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Notice_Model(Base):
    """Model for shop_point_histories."""

    __tablename__ = "notice"
    
    notice_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 		# 공지사항번호
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num")) 	# 회원번호    
    notice_title: Mapped[str] = mapped_column(String(length=128))								# 공지제목
    notice_contents: Mapped[str] = mapped_column(String(length=512))							# 공지내용
    notice_create_date: Mapped[str] = mapped_column(DateTime)									# 공지등록날짜
    