from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Board_Comments_Model(Base):
    """Model for shop_board_categories."""

    __tablename__ = "shop_board_comments"
    
    board_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_board_categories.board_categorie_num"), primary_key=True) 	# 문의번호    
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num")) 					# 회원번호    
    comment_title: Mapped[str] = mapped_column(String(length=128))												# 답글제목
    comment_content: Mapped[str] = mapped_column(String(length=512))											# 답글내용
    comment_create_date: Mapped[str] = mapped_column(DateTime)													# 답글등록날짜
    