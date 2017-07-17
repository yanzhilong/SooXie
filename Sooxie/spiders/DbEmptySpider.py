# -*- coding: utf-8 -*-
import scrapy
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.image import Image as ImageDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from Sooxie.db.property import Property as PropertyDb
from Sooxie.db.size import Size as SizeDb
from Sooxie.db.color import Color as ColorDb
from Sooxie.db.tbproperty import TbProperty as TbPropertyDb


class SooXieSpider(scrapy.Spider):
    name = "DBE"

    page = 1  # 页数
    baseurl = "https://sooxie.com/?r=all&Page="  # 爬虫首页
    # 定义入口网址
    start_urls = [baseurl + str(page), ]

    def parse(self, response):
        self.deleteall()

    def deleteall(self):
        shoedb = ShoeDb()
        imagedb = ImageDb()
        mainimagedb = MainImageDb()
        property = PropertyDb()
        sizedb = SizeDb()
        colordb = ColorDb()

        imagedb.deleteall()
        mainimagedb.deleteall()
        property.deleteall()
        sizedb.deleteall()
        colordb.deleteall()
        shoedb.deleteall()