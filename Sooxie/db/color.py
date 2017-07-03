# -*- coding: utf-8 -*-
from base import Base
from Sooxie import db
from Sooxie.db import ColorTable
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from sqlalchemy.sql import select


class Color(Base):

    def __init__(self):
        pass

    def addentry(self, entry):
        ins = ColorTable.insert().values(Id=entry.Id, Name=entry.Name, ShoeId=entry.ShoeId)
        conn = db.engine.connect()
        conn.execute(ins)

    def addentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                ins = ColorTable.insert().values(Id=entry.Id, Name=entry.Name, ShoeId=entry.ShoeId)
                connection.execute(ins)
            trans.commit()
        except Exception,e:
            print(u"添加color异常" + e.message)
            trans.rollback()

    def updateentry(self, entry):
        connection = db.engine.connect()
        stmt = ColorTable.update(). \
            where(ColorTable.c.Id == entry.Id). \
            values(Name=entry.Name, ShoeId=entry.ShoeId)
        connection.execute(stmt)

    def updateentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                stmt = ColorTable.update(). \
                    where(ColorTable.c.Id == entry.Id). \
                    values(Name=entry.Name, ShoeId=entry.ShoeId)
                connection.execute(stmt)
            trans.commit()
        except Exception, e:
            trans.rollback()

    def deleteentry(self, entry):
        connection = db.engine.connect()
        connection.execute(ColorTable.delete().where(ColorTable.c.Id == entry.Id))

    def deleteentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                connection.execute(ColorTable.delete().where(ColorTable.c.Id == entry.Id))
            trans.commit()
        except Exception, e:
            trans.rollback()

    def getbyid(self, entry):
        connection = db.engine.connect()
        s = select([ColorTable]).where(ColorTable.c.Id == entry.Id)
        row = connection.execute(s).fetchone()
        shoe = ShoeDomain()
        shoe.Id = row['Id']
        shoe.Name = row['Name']
        shoe.ShoeId = row['ShoeId']
        return shoe

    def deleteall(self):
        connection = db.engine.connect()
        connection.execute(ColorTable.delete())
