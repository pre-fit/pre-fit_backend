from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base
from sqlalchemy import ForeignKey


class Shop_Board_Categories_Model(Base):
    """Model for shop_board_categories."""

    __tablename__ = "shop_board_categories"
    
    board_categorie_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 	# 문의카테고리번호
    main_board_category_name: Mapped[str] = mapped_column(String(length=20))							# 메인카테고리명
    sub_board_category_name: Mapped[str] = mapped_column(String(length=20))								# 서브카테고리명
    