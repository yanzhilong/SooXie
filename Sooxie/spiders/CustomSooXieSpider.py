# -*- coding: utf-8 -*-
import scrapy
import time
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


import re
import uuid
from scrapy import FormRequest

shoeuls = []

from Sooxie.Repertorys.Repertory import Repertory


class SooXieSpider(scrapy.Spider):
    name = "CustomSooXie"

    page = 0  # 页数
    count = 0  # 宝贝计数

    # 定义入口网址
    start_urls = [
        'https://sooxie.com/?s=%E8%B6%B3%E6%AD%A5%E5%A4%A9%E4%B8%8B+1200&min=&max=',
    ]


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

        print(u"处理当前页面" + str(self.page + 1))
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
        if self.page == len(self.start_urls):
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

    def operatoruls(self):
        print(u'到达operatoruls' + str(self.page))
        time.sleep(1)
        if len(shoeuls) == 0:
            print(u"operatoruls" + str(len(shoeuls)))
            yield None
        else:
            self.count += 1
            print (u"处理第" + str(self.count) + u"个商品")
            ul = shoeuls.pop(0)
            shoe = ShoeDomain()
            shoe.Id = str(uuid.uuid1())
            shoe.Market = ul.css("a.scico::text").extract_first()
            # print(u"市场:" + shoe.market)
            price_num = ul.css("li.rz div.left strong::text").extract_first()
            # 判断幸福街市场及价格
            if shoe.Market is not None and shoe.Market == u"幸福街市场" and 10 < float(price_num) < 50:
                # 得到链接并请求这个页面
                details_link = ul.css("li.img a::attr(href)").extract_first()
                if details_link is not None:
                    print (u"详情url" + details_link)
                    # count += 1
                    # print (u"处理第" + str(count) + u"个商品")
                    # 发起一个请求并由详情页面处理
                    yield scrapy.Request(details_link, callback=self.show_details, meta={"shoe": shoe})
                else:
                    print (u"url不符合")
            else:
                print (u"不是幸福街:" + shoe.Market + price_num)
            print (u"继续")
            yield self.operatoruls()

    def operatorul1s(self):

        global shoeuls
        for ul in shoeuls:
            # time.sleep(10)
            self.count += 1
            print (u"处理第" + str(self.count) + u"个商品")
            shoe = ShoeDomain()
            shoe.Id = str(uuid.uuid1())
            shoe.Market = ul.css("a.scico::text").extract_first()
            # print(u"市场:" + shoe.market)
            price_num = ul.css("li.rz div.left strong::text").extract_first()
            # 判断幸福街市场及价格
            if shoe.Market is not None and shoe.Market == u"幸福街市场":
                # 得到链接并请求这个页面
                details_link = ul.css("li.img a::attr(href)").extract_first()
                if details_link is not None:
                    print (u"详情url" + details_link)
                    # count += 1
                    # print (u"处理第" + str(count) + u"个商品")
                    # 发起一个请求并由详情页面处理
                    yield scrapy.Request(details_link, callback=self.show_details, meta={"shoe": shoe})
                else:
                    print (u"url不符合")
            else:
                print (u"不是幸福街:" + shoe.Market + price_num)

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
        shoe.Sizes = self.operatorsizes(sizestmp)
        popularityandupdate = response.css("div.xgr_3_h div.xgr_3p")[2].css("strong")
        shoe.Popularity = popularityandupdate[0].css("strong::text").extract_first()
        if len(popularityandupdate) > 1:
            shoe.UpdateStr = popularityandupdate[1].css("strong font::text").extract_first()
            if shoe.UpdateStr == u'超半年未更新请联系商家确定是否下架！':
                print(u'超半年未更新')
                # yield self.operatoruls()
                return
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
            if shoe.Sort > 2:
                print(u'超过七日')
                # yield self.operatoruls()
                return
        else:
            print(u'没找到更新时间')
            # yield self.operatoruls()
            return
        colorstmp = response.css("div.xgr_3_h div.xgr_3p")[4].css("li::attr(datavalue)").extract()
        shoe.Colors = self.operatorcolors(colorstmp)
        # imagestmp = response.css("div.xgr_5 img.scrollLoading::attr(data-url)").extract()
        # self.log(u'图片大小')
        # self.log(imagestmp)
        # shoe.Images = self.operatorimages(imagestmp)
        shoeid = self.get_shoe_id(response.url)
        # shoe.No = shoeid
        # 请求鞋子参数
        healurl = response.urljoin("/handler/getSXHandler.ashx")
        # self.log(u'请求属性页面' + healurl)

        # print(u"详情页title")
        # print(shoe.Title)

        # 继续请求主要属性参数
        yield FormRequest(url=healurl,
                            formdata={'p': "xd", 'id': shoeid},
                            callback=self.getHead,
                            meta={"shoe": shoe, "shoeid": shoeid})

        # yield self.operatoruls()
    def getHead(self, response):
        print(u'到达请求鞋子属性页面')
        shoe = response.meta["shoe"]
        shoeid = response.meta["shoeid"]
        propertyemp = response.css("ul.attributes-list li::text").extract()
        shoe.Properties = self.operatorpropertys(propertyemp)
        if shoe.Properties is None or len(shoe.Properties) == 0:
            print(u'没有属性')
            shoe.Properties = []
        # shoenew = self.operatorshoe(shoe)
        # yield SooxieItem(Id=shoenew.Id, Title=shoenew.Title, Url=shoenew.Url, Number=shoenew.Number,
        #                   Price=shoenew.Price,
        #                   Popularity=shoenew.Popularity, UpdateStr=shoenew.UpdateStr, Market=shoenew.Market,
        #                   Sort=shoenew.Sort,
        #                   Sizes=shoenew.Sizes, Colors=shoenew.Colors, Images=shoenew.Images,
        #                   MainImages=shoenew.MainImages, Properties=shoenew.Properties)

        # 请求主图列表
        healurl = response.urljoin("/handler/loadImgHandler.ashx")
        # 继续请求主要属性参数
        return FormRequest(url=healurl,
                            formdata={'p': "xd", 'id': shoeid},
                            callback=self.getImages,
                            meta={"shoe": shoe})

    def get_shoe_id(self,url):
        p1 = "\\d+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, url)  # 在源文本中搜索符合正则表达式的部分
        pageid = matcher1.group(0)  # 打印出来
        return pageid

    def getImages(self, response):
        print(u'到达请求鞋子主图页面')
        shoe = response.meta["shoe"]
        mainimagestmp = response.css("img::attr(bimg)").extract()
        shoe.MainImages = self.operatormainimages(mainimagestmp)
        return self.last_action(shoe)

    def last_action(self, shoe):
        # self.count += 1
        shoenew = self.operatorshoe(shoe)
        print(u'完成第 %d 个商品' % self.count + u'的爬虫')
        # print(shoenew.Title)
        # yield shoe
        return SooxieItem(Id=shoenew.Id, Title=shoenew.Title, Url=shoenew.Url, Number=shoenew.Number, Price=shoenew.Price,
                         Popularity=shoenew.Popularity, UpdateStr=shoenew.UpdateStr, Market=shoenew.Market, Sort=shoenew.Sort,
                         Sizes=shoenew.Sizes, Colors=shoenew.Colors, Images=shoenew.Images,
                         MainImages=shoenew.MainImages, Properties=shoenew.Properties)

    def operatorsizes(self, list):
        sizeslist = []
        for si in list:
            size = SizeDomain()
            size.Id = str(uuid.uuid1())
            size.Num = si
            sizeslist.append(size)
        return sizeslist

    def operatorcolors(self, list):
        colorlist = []
        for col in list:
            color = ColorDomain()
            color.Id = str(uuid.uuid1())
            color.Name = col
            colorlist.append(color)
        return colorlist

    def operatorimages(self, list):
        imageslist = []
        sort = 0
        for ima in list:
            image = ImageDomain()
            image.Id = str(uuid.uuid1())
            image.Url = ima
            image.Sort = sort
            imageslist.append(image)
            sort += 1
        return imageslist

    def operatorpropertys(self, list):
        propertylist = []
        for pro in list:
            property = PropertyDomain()
            property.Id = str(uuid.uuid1())
            property.Name = pro.split(": ")[0]
            property.Value = pro.split(": ")[1]
            propertylist.append(property)
        return propertylist

    def operatormainimages(self, list):
        mainimagelist = []
        sort = 0
        for ima in list:
            mainimage = MainImageDomain()
            mainimage.Id = str(uuid.uuid1())
            mainimage.Url = ima
            mainimage.Sort = sort
            if mainimage.Url == u"":
                continue
            mainimagelist.append(mainimage)
            sort += 1
        return mainimagelist

    def operatorshoe(self, shoe):
        shoe.Id = str(uuid.uuid1())
        for size in shoe.Sizes:
            size.ShoeId = shoe.Id
            size.Id = str(uuid.uuid1())
        for col in shoe.Colors:
            col.ShoeId = shoe.Id
            col.Id = str(uuid.uuid1())

        for pro in shoe.Properties:
            pro.ShoeId = shoe.Id
            pro.Id = str(uuid.uuid1())
        for mima in shoe.MainImages:
            mima.ShoeId = shoe.Id
            mima.Id = str(uuid.uuid1())

        return shoe


