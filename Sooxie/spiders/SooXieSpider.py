# -*- coding: utf-8 -*-
import scrapy
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


import re
import uuid
from scrapy import FormRequest
from Sooxie.Repertorys.Repertory import Repertory


class SooXieSpider(scrapy.Spider):
    name = "SooXie"

    page = 1  # 页数
    count = 0  # 宝贝计数
    baseurl = "https://sooxie.com/?r=all&Page="  # 爬虫首页

    # 定义入口网址
    start_urls = [baseurl + str(page), ]

    def parse(self, response):

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

        # self.deleteall()
        # return
        shoe = ShoeDomain()
        shoe.Id = str(uuid.uuid1())
        print(u"处理当前页面" + str(self.page))
        # 得到所有的鞋子当前页的主页面数据
        shoeuls = response.css("ul.pro")

        for ul in shoeuls:
            self.log(u'循环遍历第%d页的商品' % self.page)
            shoe.Market = ul.css("a.scico::text").extract_first()
            # print(u"市场:" + shoe.market)
            price_num = ul.css("li.rz div.left strong::text").extract_first()
            # 判断幸福街市场及价格
            if shoe.Market is not None and shoe.Market == u"幸福街市场" and 10 < float(price_num) < 50:
                # 得到链接并请求这个页面
                details_link = ul.css("li.img a::attr(href)").extract_first()
                if details_link is not None:
                    # count += 1
                    # print (u"处理第" + str(count) + u"个商品")
                    # 发起一个请求并由详情页面处理
                    yield scrapy.Request(details_link, callback=self.show_details, meta={"shoe": shoe})
        # 得到下一页的链接并打开
        self.page += 1
        yield scrapy.Request(self.baseurl + str(self.page), callback=self.parse)

    # 搜鞋的详情页面
    def show_details(self, response):

        # self.log(u'到达详情页面')
        self.count += 1
        shoe = response.meta["shoe"]
        shoe.Url = response.url
        shoe.Title = response.css("div.xgr_3_h h2.xgr_3p::text").extract_first()
        shoe.Title = shoe.Title.strip()
        shoe.No = response.css("div.xgr_3_h div.xgr_3p strong::text").extract_first()
        shoe.Price = response.css("div.xgr_3_h div.xgr_3p em::text").extract_first()
        sizestmp  = response.css("div.xgr_3_h div.xgr_3p")[3].css("li::attr(datavalue)").extract()
        shoe.Sizes = self.operatorsizes(sizestmp)
        popularityandupdate = response.css("div.xgr_3_h div.xgr_3p")[2].css("strong")
        shoe.Popularity = popularityandupdate[0].css("strong::text").extract_first()
        if len(popularityandupdate) > 1:
            shoe.Update = popularityandupdate[1].css("strong font::text").extract_first()
        colorstmp = response.css("div.xgr_3_h div.xgr_3p")[4].css("li::attr(datavalue)").extract()
        shoe.Colors = self.operatorcolors(colorstmp)
        imagestmp = response.css("div.xgr_5 img.scrollLoading::attr(data-url)").extract()
        # self.log(u'图片大小')
        # self.log(imagestmp)
        shoe.Images = self.operatorimages(imagestmp)
        shoeid = self.get_shoe_id(response.url)
        # shoe.No = shoeid
        # 请求鞋子参数
        healurl = response.urljoin("/handler/getSXHandler.ashx")
        self.log(u'请求属性页面' + healurl)
        # 继续请求主要属性参数
        return [FormRequest(url=healurl,
                            formdata={'p': "xd", 'id': shoeid},
                            callback=self.getHead,
                            meta={"shoe": shoe, "shoeid": shoeid}), ]

    def getHead(self, response):
        self.log(u'到达请求鞋子属性页面')
        shoe = response.meta["shoe"]
        shoeid = response.meta["shoeid"]
        propertyemp = response.css("ul.attributes-list li::text").extract()
        shoe.Properties = self.operatorpropertys(propertyemp)
        if shoe.Properties is None or len(shoe.Properties) == 0:
            return
        # 请求主图列表
        healurl = response.urljoin("/handler/loadImgHandler.ashx")
        # 继续请求主要属性参数
        return [FormRequest(url=healurl,
                            formdata={'p': "xd", 'id': shoeid},
                            callback=self.getImages,
                            meta={"shoe": shoe}), ]

    def get_shoe_id(self,url):
        p1 = "\\d+"  # 这是我们写的正则表达式规则，你现在可以不理解啥意思
        pattern1 = re.compile(p1)  # 我们在编译这段正则表达式
        matcher1 = re.search(pattern1, url)  # 在源文本中搜索符合正则表达式的部分
        pageid = matcher1.group(0)  # 打印出来
        return pageid

    def getImages(self, response):
        self.log(u'到达请求鞋子主图页面')
        shoe = response.meta["shoe"]
        mainimagestmp = response.css("img::attr(bimg)").extract()
        shoe.MainImages = self.operatormainimages(mainimagestmp)
        return self.last_action(shoe)

    def last_action(self, shoe):
        self.log(u'完成第 %d 个商品' % self.count + u'的爬虫')
        shoedb = ShoeDb()
        imagedb = ImageDb()
        mainimagedb = MainImageDb()
        property = PropertyDb()
        sizedb = SizeDb()
        colordb = ColorDb()
        # if shoedb.getbyurl(shoe) is not None:
        #     self.log(u'当前商品 %d 不为空' % shoe.No)
        #     return
        shoenew = self.operatorshoe(shoe)
        shoedb.addentry(shoenew)
        imagedb.addentrys(shoe.Images)
        mainimagedb.addentrys(shoe.MainImages)
        property.addentrys(shoe.Properties)
        sizedb.addentrys(shoe.Sizes)
        colordb.addentrys(shoe.Colors)
        yield shoe

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
        for ima in list:
            image = ImageDomain()
            image.Id = str(uuid.uuid1())
            image.Url = ima
            imageslist.append(image)
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
        for ima in list:
            mainimage = MainImageDomain()
            mainimage.Id = str(uuid.uuid1())
            mainimage.Url = ima
            mainimagelist.append(mainimage)
        return mainimagelist

    def operatorshoe(self, shoe):
        self.log(u'主图片大小')
        self.log(shoe.MainImages)
        shoe.Id = str(uuid.uuid1())
        for size in shoe.Sizes:
            size.ShoeId = shoe.Id
        for col in shoe.Colors:
            col.ShoeId = shoe.Id
        for ima in shoe.Images:
            ima.ShoeId = shoe.Id
        for pro in shoe.Properties:
            pro.ShoeId = shoe.Id
        for mima in shoe.MainImages:
            mima.ShoeId = shoe.Id
        return shoe

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
