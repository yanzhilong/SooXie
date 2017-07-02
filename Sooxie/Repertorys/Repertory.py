# -*- coding: utf-8 -*-
# 导入:
from sqlalchemy import Column, String, Float, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select

metadata = MetaData()
# 宝贝实体
ShoeTable = Table('shoe', metadata,
             Column('Id', String(36), primary_key=True),
             Column('Title', String(50)),
             Column('Url', String(50)),
             Column('No', String(50)),
             Column('Price', Float),
             Column('Popularity', Integer),
             Column('Update', String(50)),
             Column('Market', String(50)),
             )

# 详情图实体
ImageTable = Table('Image', metadata,
              Column('Id', String(36), primary_key=True),
              Column('Url', String(50)),
              Column('ShoeId', None, ForeignKey('shoe.Id')),
              )

# 主图实体
MainImageTable = Table('MainImage', metadata,
                  Column('Id', String(36), primary_key=True),
                  Column('Url', String(50)),
                  Column('ShoeId', None, ForeignKey('shoe.Id')),
                  )

# 属性实体
PropertyTable = Table('Property', metadata,
                 Column('Id', String(36), primary_key=True),
                 Column('Name', String(50)),
                 Column('ShoeId', None, ForeignKey('shoe.Id')),
                 )

# 尺码实体
Size = Table('Size', metadata,
             Column('Id', String(36), primary_key=True),
             Column('Num', String(50)),
             Column('ShoeId', None, ForeignKey('shoe.Id')),
             )

# 颜色实体
Color = Table('Color', metadata,
              Column('Id', String(36), primary_key=True),
              Column('Name', String(50)),
              Column('ShoeId', None, ForeignKey('shoe.Id')),
              )


class Repertory:

    # 定义静态变量实例
    __instance = None

    def __init__(self):

        self.engine = create_engine('mysql+mysqlconnector://root:tiger@localhost:3306/sooxie')

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Repertory, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def createtable(self):

        metadata.create_all(self.engine)

    def addentry(self, table_name, list_values):
        conn = self.engine.connect()


        conn.execute(table_name.insert(), list_values)

    def updateentry(self, table_name, value, idvalue):
        stmt = table_name.update(). \
            values(value). \
            where(table_name.c.id == idvalue)
        conn = self.engine.connect()
        conn.execute(stmt)

    def deleteentry(self, table_name, idvalue):
        conn = self.engine.connect()
        conn.execute(table_name.delete().where(table_name.c.id == idvalue))

    def selectentrys(self, table_name):
        conn = self.engine.connect()
        s = select([table_name])
        result = conn.execute(s)
        return result
        for row in result:
            print "name:", row['name'], "; fullname:", row['fullname']