from typing import Dict,Any
from sqlalchemy import update,delete,insert
from sqlalchemy.future import select
from sqlalchemy.orm import Session 
from app.model.db import Member
from datetime import datetime

class MemberRepository:
    def __init__(self,sess:Session):
        self.sess:Session = sess
    
    async def insert_member(self,member:Member)->bool:
        try:
            sql = insert(Member).values(id=member.id, firstname=member.firstname, middlename=member.middlename, lastname=member.lastname,
                            email=member.email, mobile=member.mobile, role=member.role, member_date=datetime.strptime(member.member_date, '%Y-%m-%d').date())
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
        except Exception as e:
            print(e)
        return False
    
    async def update_member(self,id:int,details:Dict[str,Any])->bool:
        try:
            sql = update(Member).where(Member.id==id).values(**details)
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
        except Exception as e:
            print(e)
        return False
    
    async def delete_member(self,id:int)->bool:
        try:
            sql = delete(Member).where(Member.id==id)
            sql.execution_options(synchronize_session='fetch')
            await self.sess.execute(sql)
            await self.sess.commit()
            await self.sess.close()
            return True
        except Exception as e:
            print(e)
        return False
    
    async def select_all_member(self):
        sql = select(Member)
        sql.execution_options(synchronize_session='fetch')
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records

    async def select_one_member(self,id:int):
        sql = select(Member).where(Member.id==id)
        sql.execution_options(synchronize_session='fetch')
        q = await self.sess.execute(sql)
        records = q.scalars().all()
        await self.sess.close()
        return records
    

    

    