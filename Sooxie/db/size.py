# -*- coding: utf-8 -*-
from base import Base
from Sooxie import db
from Sooxie.db import SizeTable
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from sqlalchemy.sql import select


class Size(Base):

    def __init__(self):
        pass

    def addentry(self, entry):
        ins = SizeTable.insert().values(Id=entry.Id, Num=entry.Num, ShoeId=entry.ShoeId)
        conn = db.engine.connect()
        conn.execute(ins)

    def addentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                ins = SizeTable.insert().values(Id=entry.Id, Num=entry.Num, ShoeId=entry.ShoeId)
                connection.execute(ins)
            trans.commit()
        except Exception,e:
            print(u"添加size异常" + e.message)
            trans.rollback()

    def updateentry(self, entry):
        connection = db.engine.connect()
        stmt = SizeTable.update(). \
            where(SizeTable.c.Id == entry.Id). \
            values(Num=entry.Num, ShoeId=entry.ShoeId)
        connection.execute(stmt)

    def updateentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                stmt = SizeTable.update(). \
                    where(SizeTable.c.Id == entry.Id). \
                    values(Num=entry.Num, ShoeId=entry.ShoeId)
                connection.execute(stmt)
            trans.commit()
        except Exception, e:
            trans.rollback()

    def deleteentry(self, entry):
        connection = db.engine.connect()
        connection.execute(SizeTable.delete().where(SizeTable.c.Id == entry.Id))

    def deleteentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                connection.execute(SizeTable.delete().where(SizeTable.c.Id == entry.Id))
            trans.commit()
        except Exception, e:
            trans.rollback()

    def getbyid(self, entry):
        connection = db.engine.connect()
        s = select([SizeTable]).where(SizeTable.c.Id == entry.Id)
        row = connection.execute(s).fetchone()
        shoe = ShoeDomain()
        shoe.Id = row['Id']
        shoe.Num = row['Num']
        shoe.ShoeId = row['ShoeId']
        return shoe

    def deleteall(self):
        connection = db.engine.connect()
        connection.execute(SizeTable.delete())
