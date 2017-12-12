# -*- coding: utf-8 -*-
import scrapy
import time
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

shoeuls = []

from Sooxie.Repertorys.Repertory import Repertory


class SooXieSpider(scrapy.Spider):
    name = "SooXie"

    page = 1  # 页数
    count = 0  # 宝贝计数
    errorcount = 0  # 出错宝贝计数
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
        if self.page < 5:
            return scrapy.Request(self.baseurl + str(self.page), callback=self.parse)
        return self.operatorurls()

    def operatorurls(self):

        ul = self.popurls()
        if ul is not None:
            self.count += 1
            print (u"处理第" + str(self.count) + u"个商品")
            print (u"还有" + str(len(shoeuls)) + u"个商品")
            shoe = ShoeDomain()
            shoe.Id = str(uuid.uuid1())
            shoe.Market = ul.css("a.scico::text").extract_first()
            details_link = ul.css("li.img a::attr(href)").extract_first()
            if details_link is not None:
                print (u"详情url" + details_link)
                # count += 1
                # print (u"处理第" + str(count) + u"个商品")
                # 发起一个请求并由详情页面处理
                return scrapy.Request(details_link, callback=self.show_details, dont_filter=True, errback=self.detailserror, meta={"shoe": shoe})
            else:
                return self.operatorurls()

        # for ul in shoeuls:
        #     # time.sleep(10)

    def detailserror(self, failure):
        global errorcount
        self.errorcount += 1
        print(u'总共 %d 个商品' % self.errorcount + u'个商品爬虫失败')
        return self.operatorurls()

    def popurls(self):

        print (u"操作url")
        global shoeuls
        if len(shoeuls) > 0:
            ul = shoeuls[0]
            del shoeuls[0]
            return ul
        else:
            return None;

    def deleteall(self):
        shoedb = ShoeDb()
        shoedb.deleteall()

    # 搜鞋的详情页面
    def show_details(self, response):

        print(u'到达详情页面')

        shoe = response.meta["shoe"]
        shoe.Url = response.url
        shoe.Title = response.css("div.xgr_3_h h2.xgr_3p::text").extract_first()
        # print(u"详情页title")
        # print(shoe.Title)

        shoe.Title = shoe.Title.strip()
        shoe.Number = response.css("div.xgr_3_h div.xgr_3p strong::text").extract_first()
        shoe.Price = response.css("div.xgr_3_h div.xgr_3p em::text").extract_first()
        sizestmp  = response.css("div.xgr_3_h div.xgr_3p")[3].css("li::attr(datavalue)").extract()
        popularityandupdate = response.css("div.xgr_3_h div.xgr_3p")[2].css("strong")
        shoe.Popularity = popularityandupdate[0].css("strong::text").extract_first()
        if len(popularityandupdate) > 1:
            shoe.UpdateStr = popularityandupdate[1].css("strong font::text").extract_first()
            if shoe.UpdateStr == u'超半年未更新请联系商家确定是否下架！':
                print(u'超半年未更新')
                return self.operatoruls()
            if shoe.UpdateStr == u"今日新款，放心上传":
                shoe.Sort = 0
            elif shoe.UpdateStr == u"三日新款，放心上传":
                shoe.Sort = 1
            elif shoe.UpdateStr == u"七日新款，放心上传":
                shoe.Sort = 2
            elif shoe.UpdateStr == u"本月更新，可以上传":
                shoe.Sort = 3
            elif shoe.UpdateStr == u"三月内更新，可以上传":
                shoe.Sort = 4
            else:
                shoe.Sort = 100
        else:
            print(u'没找到更新时间')
            return None

        shoeid = self.get_shoe_id(response.url)
        # shoe.No = shoeid
        # 请求鞋子参数
        healurl = response.urljoin("/handler/getSXHandler.ashx")
        # self.log(u'请求属性页面' + healurl)

        # print(u"详情页title")
        # print(shoe.Title)

        return self.last_action(shoe)

    def get_shoe_id(self,url):
        p1 = "\\d+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, url)  # 在源文本中搜索符合正则表达式的部分
        pageid = matcher1.group(0)  # 打印出来
        return pageid

    def last_action(self, shoe):
        # self.count += 1
        shoe.Id = str(uuid.uuid1())

        yield SooxieItem(Id=shoe.Id, Title=shoe.Title, Url=shoe.Url, Number=shoe.Number, Price=shoe.Price,
                         Popularity=shoe.Popularity, UpdateStr=shoe.UpdateStr, Market=shoe.Market, Sort=shoe.Sort)
        print(u'完成第 %d 个商品' % self.count + u'的爬虫')
        global errorcount
        print(u'总共 %d 个商品' % self.errorcount + u'个商品爬虫失败')

        # print(shoenew.Title)
        yield self.operatorurls()


    def operatorshoe(self, shoe):
        shoe.Id = str(uuid.uuid1())
        for mima in shoe.MainImages:
            mima.ShoeId = shoe.Id
            mima.Id = str(uuid.uuid1())

        return shoe


