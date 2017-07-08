# -*- coding: utf-8 -*-

# 导入:
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool
from sqlalchemy import Table, Column, Integer, Float, String, MetaData, ForeignKey

engine = None
metadata = MetaData()

# 宝贝实体
ShoeTable = Table('sx_shoe', metadata,
                Column('Id', String(36), primary_key=True),
                Column('Title', String(50)),
                Column('Url', String(50)),
                Column('Number', String(50)),
                Column('Price', Float),
                Column('Popularity', Integer),
                Column('UpdateStr', String(50)),
                Column('Market', String(50)),
                Column('Sort', Integer),
                )

# 详情图实体
ImageTable = Table('sx_image', metadata,
              Column('Id', String(36), primary_key=True),
              Column('Url', String(250)),
              Column('Sort', Integer),
              Column('ShoeId', None, ForeignKey('sx_shoe.Id')),
              )

# 主图实体
MainImageTable = Table('sx_mainimage', metadata,
                  Column('Id', String(36), primary_key=True),
                  Column('Url', String(250)),
                  Column('Sort', Integer),
                  Column('ShoeId', None, ForeignKey('sx_shoe.Id')),
                  )

# 属性实体
PropertyTable = Table('sx_property', metadata,
                     Column('Id', String(36), primary_key=True),
                     Column('Name', String(50)),
                     Column('Value', String(50)),
                     Column('ShoeId', None, ForeignKey('sx_shoe.Id')),
                     )

# 尺码实体
SizeTable = Table('sx_size', metadata,
             Column('Id', String(36), primary_key=True),
             Column('Num', Integer),
             Column('ShoeId', None, ForeignKey('sx_shoe.Id')),
             )

# 颜色实体
ColorTable = Table('sx_color', metadata,
              Column('Id', String(36), primary_key=True),
              Column('Name', String(50)),
              Column('ShoeId', None, ForeignKey('sx_shoe.Id')),
              )

# 淘宝属性实体
TbPropertyTable = Table('tb_property', metadata,
              Column('Id', String(36), primary_key=True),
              Column('Name', String(45)),
              Column('ValueKey', String(45)),
              Column('TbPropertyCategoryId', String(36)),
              )

def init_db_engine(connect_str):
    global engine
    engine = create_engine(connect_str, poolclass=NullPool)


def create_table():
    metadata.create_all(engine)
