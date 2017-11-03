# -*- coding: utf-8 -*-
import scrapy
from Sooxie.domain.Sooxie import *
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from Sooxie.domain.Shoe import MainImage as MainImageDomain
from Sooxie.db.shoe import Shoe as ShoeDb
from Sooxie.db.mainimage import MainImage as MainImageDb
from Sooxie.items import SooxieItem
from Sooxie import db

import re
import uuid
from scrapy import FormRequest
from Sooxie.Repertorys.Repertory import Repertory


class SooXieSpider(scrapy.Spider):
    name = "Sooxie"

    page = 1  # 页数
    count = 0  # 宝贝计数
    baseurl = "https://sooxie.com/?r=all&Page="  # 爬虫首页

    # 定义入口网址
    start_urls = [baseurl + str(page), ]
    shoeuls = []
    isinit = False

    def parse(self, response):

        yield SooxieItem(Id=str(uuid.uuid1()), Title='title1')
        return
        yield SooxieItem(Id=str(uuid.uuid1()), Title='title2')
        yield
