from typing import List, Optional
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.db.dependencies import get_db_session
from fastapi.db.models.shop_members import Shop_Members_Models

class Shop_Members_DAO:
	"""Class for Shop Members table."""

	def __init__(self, session: AsyncSession = Depends(get_db_session)):
		self.session = session

	async def create_shop_member_model(self, member_num: int) -> None:
		"""
		Add single shop_members to sesison.

		Args:
			name (str): name of shop_member
		"""
		self.session.add(Shop_Members_Models(member_num=member_num))

	async def get_all_shop_members(self, limit: int, offset: int) -> List[Shop_Members_Models]:
		"""Get all shop_members with limit/offset pagination

		Args:
			limit (int): limit of shop_members
			offset (int): offset of shop_members

		Returns:
			List[Shop_Members_Models]: stream of shop_members
		"""
		raw_shop_members = await self.session.execute(
			select(Shop_Members_Models).limit(limit).offset(offset),
		)
		return list(raw_shop_members.scalars().fetchall())

	async def filter_id(
		self,
		member_id: Optional[str] = None,
	) -> List[Shop_Members_Models]:
		"""Get specific shop_members from id

		Args:
			member_id (Optional[str], optional): id of shop_members instance

		Returns:
			List[Shop_Members_Models]: shop_members
		"""
		query = select(Shop_Members_Models)
		if id:
			query = query.where(Shop_Members_Models.member_id == id)
		rows = await self.session.execute(query)
		return list(rows.scalars().fetchall())
