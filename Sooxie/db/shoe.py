# -*- coding: utf-8 -*-
from base import Base
from Sooxie import db
from Sooxie.db import ShoeTable
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from sqlalchemy.sql import select


class Shoe(Base):

    def __init__(self):
        pass

    def addentry(self, entry):
        ins = ShoeTable.insert().values(Id=entry.Id, Title=entry.Title, Url=entry.Url, No=entry.No, Price=entry.Price,
                                        Popularity=entry.Popularity, Update=entry.Update, Market=entry.Market)
        conn = db.engine.connect()
        conn.execute(ins)

    def addentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                ins = ShoeTable.insert().values(Id=entry.Id, Title=entry.Title, Url=entry.Url, No=entry.No,
                                                Price=entry.Price,
                                                Popularity=entry.Popularity, Update=entry.Update, Market=entry.Market)
                connection.execute(ins)
            trans.commit()
        except Exception,e:
            trans.rollback()

    def updateentry(self, entry):
        connection = db.engine.connect()
        stmt = ShoeTable.update(). \
            where(ShoeTable.c.Id == entry.Id). \
            values(Title=entry.Title, Url=entry.Url, No=entry.No, Price=entry.Price, Popularity=entry.Popularity, Update=entry.Update, Market=entry.Market)
        connection.execute(stmt)

    def updateentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                stmt = ShoeTable.update(). \
                    where(ShoeTable.c.Id == entry.Id). \
                    values(Title=entry.Title, Url=entry.Url, No=entry.No,
                           Price=entry.Price,
                           Popularity=entry.Popularity, Update=entry.Update, Market=entry.Market)
                connection.execute(stmt)
            trans.commit()
        except Exception, e:
            trans.rollback()

    def deleteentry(self, entry):
        connection = db.engine.connect()
        connection.execute(ShoeTable.delete().where(ShoeTable.c.Id == entry.Id))

    def deleteentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                connection.execute(ShoeTable.delete().where(ShoeTable.c.Id == entry.Id))
            trans.commit()
        except Exception, e:
            trans.rollback()

    def getbyid(self, entry):
        connection = db.engine.connect()
        s = select([ShoeTable]).where(ShoeTable.c.Id == entry.Id)
        row = connection.execute(s).fetchone()
        shoe = ShoeDomain()
        shoe.Id = row['Id']
        shoe.Title = row['Title']
        shoe.Url = row['Url']
        shoe.No = row['No']
        shoe.Price = row['Price']
        shoe.Popularity = row['Popularity']
        shoe.Update = row['Update']
        shoe.Market = row['Market']
        return shoe

    def getbyurl(self, entry):
        connection = db.engine.connect()
        s = select([ShoeTable]).where(ShoeTable.c.Url == entry.Url)
        row = connection.execute(s).fetchone()
        if row is None:
            return None
        shoe = ShoeDomain()
        shoe.Id = row['Id']
        shoe.Title = row['Title']
        shoe.Url = row['Url']
        shoe.No = row['No']
        shoe.Price = row['Price']
        shoe.Popularity = row['Popularity']
        shoe.Update = row['Update']
        shoe.Market = row['Market']
        return shoe

    def deleteall(self):
        connection = db.engine.connect()
        connection.execute(ShoeTable.delete())
