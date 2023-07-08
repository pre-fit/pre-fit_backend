from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import String, DateTime, Integer, Boolean
from datetime import datetime
from fastapi.db.base import Base


class Shop_Members_Model(Base):
    """Model for demo purpose."""

    __tablename__ = "shop_members"

    member_num: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) 	# 회원번호
    member_id: Mapped[str] = mapped_column(String(length=20))  								# 회원아이디
    member_name: Mapped[str] = mapped_column(String(length=50))  							# 회원이름
    member_password: Mapped[str] = mapped_column(String(length=50))  						# 회원비밀번호
    member_phone: Mapped[str] = mapped_column(String(length=20))  							# 회원연락처
    member_gender: Mapped[str] = mapped_column(Boolean)  									# 회원성별
    member_birthday: Mapped[str] = mapped_column(DateTime)  								# 회원생일
    member_point: Mapped[str] = mapped_column(Integer)  									# 회원포인트
    member_email: Mapped[str] = mapped_column(String(length=256)) 							# 회원이메일
    member_grade: Mapped[str] = mapped_column(Integer)  									# 회원등급
    member_join_date: Mapped[str] = mapped_column(DateTime)  								# 회원가입일
    member_leave_date: Mapped[str] = mapped_column(DateTime)  								# 회원탈퇴일
    member_join_falg: Mapped[str] = mapped_column(Boolean) 									# 회원탈퇴여부
    member_active: Mapped[str] = mapped_column(Boolean)  									# 회원활성화여부
    member_terms_of_service: Mapped[str] = mapped_column(Boolean) 							# 서비스이용약관동의여부
    member_privacy_policy: Mapped[str] = mapped_column(Boolean) 							# 개인정보처리방침동의여부
    member_recive_marketing_info: Mapped[str] = mapped_column(Boolean)						# 마케팅정보수신동의여부
    member_approve: Mapped[str] = mapped_column(Boolean)  									# 관리자승인
    member_recommender: Mapped[str] = mapped_column(String(length=20))  					# 추천인
    
    def __init__(self, member_num, member_id, member_name, member_password, member_phone, member_gender, member_birthday, member_email,member_recommender):
        self.member_num = member_num
        self.member_id = member_id
        self.member_name = member_name
        self.member_password = member_password
        self.member_phone = member_phone
        self.member_gender = member_gender
        self.member_birthday = member_birthday
        self.member_point = 0
        self.member_email = member_email
        self.member_grade = 0
        self.member_join_date = datetime.now()
        self.member_leave_date = None
        self.member_join_falg = True
        self.memeber_active = True
        self.member_terms_of_service = False
        self.member_privacy_policy = False
        self.member_recive_marketing_info = False
        self.member_approve = True
        self.member_recommender = member_recommender
