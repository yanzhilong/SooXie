# -*- coding: utf-8 -*-
import os

import Image
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
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

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

        self.change_image_620()

    def change_image_620(self):
        rootdir = "d:\sooxie"
        excludes = ['csv', '620']
        for root, dir, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            dir[:] = [d for d in dir if d not in excludes]
            for filename in filenames:  # 输出文件信息
                infile = os.path.join(root, filename)  # 输出文件路径信息
                outfile = os.path.join("d:\\sooxie\\620", filename)  # 输出文件路径信息
                if os.path.exists(outfile):
                    continue
                print filename
                print u"文件夹信息:" + infile  # 输出文件路径信息
                print u"输出文件夹信息:" + outfile  # 输出文件路径信息
                im = Image.open(infile)
                (x, y) = im.size  # read image size
                x_s = 620  # define standard width
                y_s = y * x_s / x  # calc height based on standard width
                out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
                out.save(outfile)

    def saveimage(self, image):
        url = image.Url
        filename = "d:\\sooxie\\"
        filepath = ""
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'\d{6,}.*.(jpg|png|gif)')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match = re.search(pattern, url)
        if match is None:
            print("None")
            print(url)
        else:
            print(url)
        newname = match.group(0)
        newname = newname.replace("/", "")
        newname = newname.replace("!bac", "")
        # print(newname)
        if newname:
            # 使用Match获得分组信息
            filepath = filename + newname
            if os.path.exists(filepath):
                return
            # print(url)
            # print(filepath)
            urllib.urlretrieve(url, filepath)




    def savemainimage(self, mainimage):
        url = mainimage.Url
        filename = "d:\\sooxie\\csv\\"
        filepath = ""
        # 将正则表达式编译成Pattern对象
        pattern = re.compile(r'\d{6,}.*\.')
        # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
        match = re.search(pattern, url)
        # print(url)
        newname = match.group(0) + 'tbi'
        # print(newname)
        if newname:
            # 使用Match获得分组信息
            filepath = filename + newname
            if os.path.exists(filepath):
                return
            # print(url)
            # print(filepath)
            urllib.urlretrieve(url, filepath)