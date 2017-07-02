# -*- coding: utf-8 -*-
from base import Base
from Sooxie import db
from Sooxie.db import ImageTable
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from sqlalchemy.sql import select


class Image(Base):

    def __init__(self):
        pass

    def addentry(self, entry):
        ins = ImageTable.insert().values(Id=entry.Id, Url=entry.Url, ShoeId=entry.ShoeId)
        conn = db.engine.connect()
        conn.execute(ins)

    def addentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                ins = ImageTable.insert().values(Id=entry.Id, Url=entry.Url, ShoeId=entry.ShoeId)
                connection.execute(ins)
            trans.commit()
        except Exception,e:
            trans.rollback()

    def updateentry(self, entry):
        connection = db.engine.connect()
        stmt = ImageTable.update(). \
            where(ImageTable.c.Id == entry.Id). \
            values(Url=entry.Url, ShoeId=entry.ShoeId)
        connection.execute(stmt)

    def updateentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                stmt = ImageTable.update(). \
                    where(ImageTable.c.Id == entry.Id). \
                    values(Url=entry.Url, ShoeId=entry.ShoeId)
                connection.execute(stmt)
            trans.commit()
        except Exception, e:
            trans.rollback()

    def deleteentry(self, entry):
        connection = db.engine.connect()
        connection.execute(ImageTable.delete().where(ImageTable.c.Id == entry.Id))

    def deleteentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                connection.execute(ImageTable.delete().where(ImageTable.c.Id == entry.Id))
            trans.commit()
        except Exception, e:
            trans.rollback()

    def getbyid(self, entry):
        connection = db.engine.connect()
        s = select([ImageTable]).where(ImageTable.c.Id == entry.Id)
        row = connection.execute(s).fetchone()
        shoe = ShoeDomain()
        shoe.Id = row['Id']
        shoe.Url = row['Url']
        shoe.ShoeId = row['ShoeId']
        return shoe
