# -*- coding: utf-8 -*-
import scrapy
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.mainimage import MainImage as MainImageDb


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
        mainimagedb = MainImageDb()
        mainimagedb.deleteall()
        shoedb.deleteall()