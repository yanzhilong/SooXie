# -*- coding: utf-8 -*-
import scrapy
import time
from Sooxie.domain.Sooxie import *
from Sooxie.domain.Shoe import Shoe as ShoeDomain
from Sooxie.domain.Shoe import Company as CompanyDomain
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
from Sooxie.items import SooxieCompany
from Sooxie import db


import re
import uuid
from scrapy import FormRequest

shoeuls = []

from Sooxie.Repertorys.Repertory import Repertory


class SooXieSpider(scrapy.Spider):
    name = "AllSooXieCompany"

    page = 1  # 页数
    count = 0  # 宝贝计数
    baseurl = "https://www.sooxie.com/?r=all&Page="  # 爬虫首页

    # 定义入口网址
    start_urls = [baseurl + str(page), ]

    isinit = False
    def parse(self, response):

        global shoeuls
        global count
        # # 增加
        # shoedomain = ShoeDomain()
        # shoedomain.Id = str(uuid.uuid1())
        # shoedomain.Title = "hello"
        # shoedb = ShoeDb()
        # shoedb.addentry(shoedomain)

        # 增加多个
        # shoedomain = ShoeDomain()
        # shoedomain.Id = str(uuid.uuid1())
        # shoedomain.Title = "hello3"
        #
        # shoedomain1 = ShoeDomain()
        # shoedomain1.Id = str(uuid.uuid1())
        # shoedomain1.Title = "hello4"
        # list = [shoedomain, shoedomain1]
        #
        # shoedb = ShoeDb()
        # shoedb.addentrys(list)

        # 删除
        # shoedomain = ShoeDomain()
        # shoedomain.Id = '692f5a21-5ed7-11e7-89a1-00242cf600ed'
        # shoedb = ShoeDb()
        # shoedb.deleteentry(shoedomain)

        # 删除多个
        # shoedomain = ShoeDomain()
        # shoedomain.Id = "afba3fb0-5ee5-11e7-832b-00242cf600ed"
        #
        # shoedomain1 = ShoeDomain()
        # shoedomain1.Id = "c2f5a64f-5ee5-11e7-8303-00242cf600ed"
        # list = [shoedomain, shoedomain1]
        #
        # shoedb = ShoeDb()
        # shoedb.deleteentrys(list)

        # 查询
        # shoedomain = ShoeDomain()
        # shoedomain.Id = '2467a230-5ee6-11e7-bd50-00242cf600ed'
        # shoedb = ShoeDb()
        # shoe = shoedb.getbyid(shoedomain)
        # print(shoe.Title)

        # db.create_table()
        if not self.isinit:
            self.deleteall()
            self.isinit = True
        # return

        print(u"处理当前页面" + str(self.page))
        # 得到所有的鞋子当前页的主页面数据
        shoeulpage = response.css("ul.pro")
        for ul in shoeulpage:
            shoeuls.append(ul)
        # shoeldetaillinks = []
        # count = 0;
        # for ul in shoeuls:
        #     shoe = ShoeDomain()
        #     shoe.Id = str(uuid.uuid1())
        #     # self.log(u'循环遍历第%d页的商品' % self.page)
        #     shoe.Market = ul.css("a.scico::text").extract_first()
        #     # print(u"市场:" + shoe.market)
        #     price_num = ul.css("li.rz div.left strong::text").extract_first()
        #     # 判断幸福街市场及价格
        #     if shoe.Market is not None and shoe.Market == u"幸福街市场" and 10 < float(price_num) < 50:
        #         # 得到链接并请求这个页面
        #         details_link = ul.css("li.img a::attr(href)").extract_first()
        #         if details_link is not None:
        #             # print (u"详情url" + details_link)
        #             shoeldetaillinks.append(details_link)
        #             self.count += 1
        #             print (u"处理第" + str(self.count) + u"个商品")
        #             # 发起一个请求并由详情页面处理
        #             yield scrapy.Request(details_link, callback=self.show_details, meta={"shoe": shoe})
                    # count = count + 1
                    # if count == 2:
                    #     return

        # 得到下一页的链接并打开
        self.page += 1
        if self.page < 100:
            return scrapy.Request(self.baseurl + str(self.page), callback=self.parse)
        return self.operatorul1s()

    def makeshoeurls(self):
        print(u"makeshoeurls")
        self.page += 1
        print(u"makeshoeurls" + str(self.page))
        if self.page < 20:
            print(u"当前页面" + str(self.page))
            return scrapy.Request(self.baseurl + str(self.page), callback=self.parse)
        else:
            print(u"结束页面" + str(self.page))
            return None

    def operatorul1s(self):

        global shoeuls
        for ul in shoeuls:
            # time.sleep(10)
            self.count += 1
            print (u"处理第" + str(self.count) + u"个商品")
            company = CompanyDomain()
            company.Id = str(uuid.uuid1())
            Market = ul.css("a.scico::text").extract_first()
            # print(u"市场:" + shoe.market)
            price_num = ul.css("li.rz div.left strong::text").extract_first()
            # 判断幸福街市场及价格
            if Market is not None and Market == u"幸福街市场":
                # 得到链接并请求这个页面
                details_link = ul.css("li.img a::attr(href)").extract_first()
                if details_link is not None:
                    print (u"详情url" + details_link)
                    # count += 1
                    # print (u"处理第" + str(count) + u"个商品")
                    # 发起一个请求并由详情页面处理
                    yield scrapy.Request(details_link, callback=self.show_details, meta={"company": company})
                else:
                    print (u"url不符合")
            else:
                print (u"不是幸福街:" + Market + price_num)

    # 搜鞋的详情页面
    def show_details(self, response):

        print(u'到达详情页面')

        company = response.meta["company"]
        company.Url = response.css("div.bdomain a::attr(href)").extract_first()
        company.Title = response.css("div.bname ::text").extract_first()

        yield SooxieCompany(Id=company.Id, Title=company.Title, Url=company.Url)

