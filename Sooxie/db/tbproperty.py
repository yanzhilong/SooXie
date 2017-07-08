# -*- coding: utf-8 -*-
from base import Base
from Sooxie import db
from Sooxie.db import TbPropertyTable
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from sqlalchemy.sql import select


class TbProperty(Base):

    def __init__(self):
        pass

    def addentry(self, entry):
        ins = TbPropertyTable.insert().values(Id=entry.Id, Name=entry.Name, ValueKey=entry.ValueKey, TbPropertyCategoryId=entry.TbPropertyCategoryId)
        conn = db.engine.connect()
        conn.execute(ins)

    def addentrys(self, entrys):
        connection = db.engine.connect()
        trans = connection.begin()
        try:
            for entry in entrys:
                ins = TbPropertyTable.insert().values(Id=entry.Id, Name=entry.Name, ValueKey=entry.ValueKey, TbPropertyCategoryId=entry.TbPropertyCategoryId)
                connection.execute(ins)
            trans.commit()
        except Exception,e:
            print(u"添加property异常" + e.message)
            trans.rollback()
