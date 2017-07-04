# -*- coding: utf-8 -*-

# 导入:
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey

engine = None
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
              Column('Url', String(250)),
              Column('ShoeId', None, ForeignKey('shoe.Id')),
              )

# 主图实体
MainImageTable = Table('MainImage', metadata,
                  Column('Id', String(36), primary_key=True),
                  Column('Url', String(250)),
                  Column('ShoeId', None, ForeignKey('shoe.Id')),
                  )

# 属性实体
PropertyTable = Table('Property', metadata,
                     Column('Id', String(36), primary_key=True),
                     Column('Name', String(50)),
                     Column('Value', String(50)),
                     Column('ShoeId', None, ForeignKey('shoe.Id')),
                     )

# 尺码实体
SizeTable = Table('Size', metadata,
             Column('Id', String(36), primary_key=True),
             Column('Num', Integer),
             Column('ShoeId', None, ForeignKey('shoe.Id')),
             )

# 颜色实体
ColorTable = Table('Color', metadata,
              Column('Id', String(36), primary_key=True),
              Column('Name', String(50)),
              Column('ShoeId', None, ForeignKey('shoe.Id')),
              )


def init_db_engine(connect_str):
    global engine
    engine = create_engine(connect_str, poolclass=NullPool)


def create_table():
    metadata.create_all(engine)
