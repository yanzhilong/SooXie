# -*- coding: utf-8 -*-
import scrapy
import re
from Sooxie.domain.Sooxie import *
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from Sooxie.domain.Shoe import Image as ImageDomain
from Sooxie.domain.Shoe import MainImage as MainImageDomain
from Sooxie.domain.Shoe import Property as PropertyDomain
from Sooxie.domain.Shoe import Size as SizeDomain
from Sooxie.domain.Shoe import Color as ColorDomain
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.image import Image as ImageDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from Sooxie.db.property import Property as PropertyDb
from Sooxie.db.size import Size as SizeDb
from Sooxie.db.color import Color as ColorDb
from Sooxie.items import SooxieItem
from Sooxie import db
import urllib
import re
import uuid
from scrapy import FormRequest
from Sooxie.Repertorys.Repertory import Repertory


# 下载图片
class SooXieSpider(scrapy.Spider):
    name = "DI"

    baseurl = "https://sooxie.com/?r=all&Page=1"  # 爬虫首页

    # 定义入口网址
    start_urls = [baseurl, ]

    def parse(self, response):

        imagedb = ImageDb()
        mainimagedb = MainImageDb()
        imageslist = imagedb.getentrys()
        mainimageslist = mainimagedb.getentrys();
        # print(imageslist)
        # image = imageslist[0]
        # self.saveimage(image)
        # self.savemainimage(image)

        for image in imageslist:
            self.saveimage(image)

        for image in mainimageslist:
            self.savemainimage(image)

    def saveimage(self, image):
        url = image.Url
        filename = "d:\\sooxie\\"
        filepath = ""
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'\d.*\.[A-Za-z]{3}')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match = re.search(pattern, url)
        if match is None:
            print("None")
            print(url)
        else:
            print(url)
        newname = match.group(0)
        # print(newname)
        if newname:
            # 使用Match获得分组信息
            filepath = filename + newname
            # print(url)
            # print(filepath)
            urllib.urlretrieve(url, filepath)




    def savemainimage(self, mainimage):
        url = mainimage.Url
        filename = "d:\\sooxie\\csv\\"
        filepath = ""
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'\d.*\.')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match = re.search(pattern, url)
        # print(url)
        newname = match.group(0) + 'tbi'
        # print(newname)
        if newname:
            # 使用Match获得分组信息
            filepath = filename + newname
            # print(url)
            # print(filepath)
            urllib.urlretrieve(url, filepath)