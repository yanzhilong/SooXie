# -*- coding: utf-8 -*-
import scrapy
import Image
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
        rootdir = "d:\\sooxieimg\\"
        for root, dir, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for filename in filenames:  # 输出文件信息
                infile = os.path.join(root, filename)  # 输出文件路径信息
                outfile = os.path.join("d:\\sooxie620img\\", filename)  # 输出文件路径信息
                print filename
                print u"文件夹信息:" + infile  # 输出文件路径信息
                im = Image.open(infile)
                (x, y) = im.size #read image size
                x_s = 620 #define standard width
                y_s = y * x_s / x #calc height based on standard width
                out = im.resize((x_s, y_s), Image.ANTIALIAS) #resize image with high-quality
                out.save(outfile)