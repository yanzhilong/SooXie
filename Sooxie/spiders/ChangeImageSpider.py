# -*- coding: utf-8 -*-
import scrapy
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.image import Image as ImageDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from Sooxie.db.property import Property as PropertyDb
from Sooxie.db.size import Size as SizeDb
from Sooxie.db.color import Color as ColorDb
from Sooxie.db.tbproperty import TbProperty as TbPropertyDb
import os
import os.path

class SooXieSpider(scrapy.Spider):
    name = "CI"

    page = 1  # 页数
    baseurl = "https://sooxie.com/?r=all&Page="  # 爬虫首页
    # 定义入口网址
    start_urls = [baseurl + str(page), ]

    def parse(self, response):
        rootdir = "d:\data"
        for filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for filename in filenames:  # 输出文件信息
            print "parent is": + parent
            print "filename is:" + filename
            print "the full name of the file is:" + os.path.join(parent, filename)  # 输出文件路径信息
