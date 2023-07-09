import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Question_Boards_Model(Base):
    """Model for shop_question_boards."""

    __tablename__ = "shop_question_boards"
    
    board_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 								# 공지사항번호
    board_categorie_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_board_categories.board_categorie_num")) 	# 문의카테고리번호    
    member_num: Mapped[int] = mapped_column(Integer, ForeignKey("shop_members.member_num")) 							# 회원번호    
    board_create_date: Mapped[datetime] = mapped_column(DateTime)															# 문의날짜
    board_title: Mapped[str] = mapped_column(String(length=128))														# 문의제목
    board_contests: Mapped[str] = mapped_column(String(length=512))														# 문의내용
    board_is_answered: Mapped[bool] = mapped_column(Boolean)																# 답글여부
    